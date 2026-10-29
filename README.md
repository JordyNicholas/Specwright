# Specwright

Specwright is not a language model. It is a tool that orchestrates AI agents through a software project: from an idea prompt, through a proposal, an architecture, requirements, and a team charter you accept, to a project folder and one development cycle.

The folder is readable without Git. Agents draft. You accept. LangGraph orders the work. LangChain calls the model. A CrewAI crew may talk inside one stage.

**Status:** the scaffold is in place (`/health` only). The product pass is specified and not built yet. The ordered work is the [product backlog](docs/reference/backlog.md).

## Documentation

Human-facing docs follow [Diátaxis](https://diataxis.fr/). Start at the [docs map](docs/README.md).

| If you need to | Go to |
|---|---|
| Learn by doing | [Tutorial: run the scaffold](docs/tutorials/run-the-scaffold.md) |
| Complete a task | [How-to guides](docs/how-to/run-quality-gates.md) |
| Look up a fact | [Reference](docs/reference/requirements.md) |
| Understand why | [Explanation](docs/explanation/product.md) |

## Run the scaffold

```bash
make setup
make check
make run
```

Open `http://127.0.0.1:8000/health`. The lesson with expected output is the [tutorial](docs/tutorials/run-the-scaffold.md).

## License

MIT. See [LICENSE](LICENSE).
