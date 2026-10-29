#!/usr/bin/env python3
"""Move SpecWright stories when a pull request is linked or merged.

A pull request that closes an issue moves that issue to In review.
Merging that pull request moves it from In review to Done.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

PROJECT_LOGIN = "JordyNicholas"
PROJECT_NUMBER = 8
REVIEW = "In review"
DONE = "Done"
TO_REVIEW = {"Product backlog", "Ready", "In progress"}


def gql(query: str, variables: dict) -> dict:
    payload = json.dumps({"query": query, "variables": variables}).encode()
    completed = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=payload,
        capture_output=True,
        check=False,
    )
    body = json.loads(completed.stdout.decode() or "{}")
    if completed.returncode != 0 or body.get("errors"):
        sys.stderr.write(json.dumps(body.get("errors") or completed.stderr.decode(), indent=2))
        sys.stderr.write("\n")
        raise SystemExit(1)
    return body["data"]


def desired_status(current: str, merged: bool) -> str | None:
    if merged and current == REVIEW:
        return DONE
    if not merged and current in TO_REVIEW:
        return REVIEW
    return None


def project_status() -> tuple[str, dict[str, str]]:
    data = gql(
        """
        query($login: String!, $number: Int!) {
          user(login: $login) {
            projectV2(number: $number) {
              fields(first: 30) {
                nodes {
                  ... on ProjectV2SingleSelectField {
                    id
                    name
                    options { id name }
                  }
                }
              }
            }
          }
        }
        """,
        {"login": PROJECT_LOGIN, "number": PROJECT_NUMBER},
    )
    for field in data["user"]["projectV2"]["fields"]["nodes"]:
        if field and field.get("name") == "Status":
            return field["id"], {option["name"]: option["id"] for option in field["options"]}
    raise SystemExit("Status field not found")


def closing_issue_numbers(owner: str, name: str, pr_number: int) -> list[int]:
    data = gql(
        """
        query($owner: String!, $name: String!, $number: Int!) {
          repository(owner: $owner, name: $name) {
            pullRequest(number: $number) {
              closingIssuesReferences(first: 50) { nodes { number } }
            }
          }
        }
        """,
        {"owner": owner, "name": name, "number": pr_number},
    )
    nodes = data["repository"]["pullRequest"]["closingIssuesReferences"]["nodes"]
    return [node["number"] for node in nodes]


def issue_project_item(owner: str, name: str, issue_number: int) -> tuple[str, str] | None:
    data = gql(
        """
        query($owner: String!, $name: String!, $number: Int!) {
          repository(owner: $owner, name: $name) {
            issue(number: $number) {
              projectItems(first: 20) {
                nodes {
                  id
                  project { number }
                  fieldValues(first: 20) {
                    nodes {
                      ... on ProjectV2ItemFieldSingleSelectValue {
                        name
                        field { ... on ProjectV2SingleSelectField { name } }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """,
        {"owner": owner, "name": name, "number": issue_number},
    )
    for item in data["repository"]["issue"]["projectItems"]["nodes"]:
        if item["project"]["number"] != PROJECT_NUMBER:
            continue
        for value in item["fieldValues"]["nodes"]:
            field = value.get("field") or {}
            if field.get("name") == "Status":
                return item["id"], value["name"]
    return None


def set_status(item_id: str, field_id: str, option_id: str) -> None:
    gql(
        """
        mutation($input: UpdateProjectV2ItemFieldValueInput!) {
          updateProjectV2ItemFieldValue(input: $input) { projectV2Item { id } }
        }
        """,
        {
            "input": {
                "projectId": os.environ["PROJECT_ID"],
                "itemId": item_id,
                "fieldId": field_id,
                "value": {"singleSelectOptionId": option_id},
            }
        },
    )


def main() -> None:
    if os.environ.get("MERGED", "false") != "true" and os.environ.get("EVENT") == "closed":
        print("pull request closed without merge")
        return
    merged = os.environ.get("MERGED", "false") == "true"
    owner, name = os.environ["REPOSITORY"].split("/", 1)
    pr_number = int(os.environ["PR_NUMBER"])
    field_id, options = project_status()
    project_id = gql(
        """
        query($login: String!, $number: Int!) {
          user(login: $login) {
            projectV2(number: $number) { id }
          }
        }
        """,
        {"login": PROJECT_LOGIN, "number": PROJECT_NUMBER},
    )["user"]["projectV2"]["id"]
    os.environ["PROJECT_ID"] = project_id

    for issue_number in closing_issue_numbers(owner, name, pr_number):
        found = issue_project_item(owner, name, issue_number)
        if found is None:
            print(f"#{issue_number} is not on the board")
            continue
        item_id, current = found
        target = desired_status(current, merged)
        if target is None:
            print(f"#{issue_number} stays {current}")
            continue
        set_status(item_id, field_id, options[target])
        print(f"#{issue_number} {current} -> {target}")


if __name__ == "__main__":
    main()
