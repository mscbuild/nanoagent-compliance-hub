# nanoagent-compliance-hub

Simple ReAct agent
Agent generated with `agents-cli` version `0.5.0`

## Project Structure

```
nanoagent-compliance-hub/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── workflow.py
│   ├── config.py
│   ├── database.py
│   ├── repository.py
│   └── models.py
│
├── agents/
│   ├── __init__.py
│   ├── security_agent.py
│   ├── compliance_agent.py
│   ├── risk_agent.py
│   └── manager_agent.py
│
├── skills/
│   ├── __init__.py
│   ├── compliance_skill.py
│   ├── reporting_skill.py
│   └── risk_skill.py
│
├── mcp_server/
│   ├── __init__.py
│   └── expense_policy_server.py
│
├── dashboard/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── static/
│   │   └── styles.css
│   │
│   └── templates/
│       └── index.html
│
├── tests/
│   ├── __init__.py
│   ├── test_security.py
│   ├── test_workflow.py
│   └── test_mcp_server.py
│
├── docs/
│   ├── architecture.md
│   ├── threat_model.md
│   ├── deployment.md
│   └── screenshots/
│       ├── cover.png
│       ├── dashboard.png
│       ├── injection_detection.png
│       └── mcp_architecture.png
│
├── sample_expenses/
│   ├── low_value.json
│   ├── conference.json
│   ├── prompt_injection.json
│   └── pii_expense.json
│
├── scripts/
│   ├── seed_demo_data.py
│   └── reset_database.py
│
└── .github/
    └── workflows/
        └── tests.yml
```

> 💡 **Tip:** Use [Gemini CLI](https://github.com/google-gemini/gemini-cli) for AI-assisted development - project context is pre-configured in `GEMINI.md`.

## Requirements

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/) ([add packages](https://docs.astral.sh/uv/concepts/dependencies/) with `uv add <package>`)
- **agents-cli**: Agents CLI - Install with `uv tool install google-agents-cli`
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)


## Quick Start

Install `agents-cli` and its skills if not already installed:

```bash
uvx google-agents-cli setup
```

Install required packages:

```bash
agents-cli install
```

Test the agent with a local web server:

```bash
agents-cli playground
```

You can also use features from the [ADK](https://adk.dev/) CLI with `uv run adk`.

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli eval`    | Evaluate agent behavior (generate, grade, analyze, and more — see `agents-cli eval --help`) |
| `uv run pytest tests/unit tests/integration` | Run unit and integration tests                                                        |

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.
