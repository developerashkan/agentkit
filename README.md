# agentkit

A production-ready starter toolkit for building modular Python AI agents.

## Core Modules

- **Core Agent Engine** (`agentkit.engine`): modular async task runner with concurrency control.
- **Claude Skills Compatibility** (`agentkit.skills`): manifest loader/validator plus template generation.
- **CLI Developer Toolkit** (`agentkit.cli`): scaffold projects, generate skill templates, and record metrics events.
- **Pre-built Connectors** (`agentkit.connectors`): webhook payloads for Slack/Teams/Discord and file ingestion for RAG pipelines.
- **Real-time Logging + Metrics** (`agentkit.logging_metrics`): lightweight event counters for usage/star telemetry.
- **Deployment Support**: Dockerfile and GitHub Actions workflow template included.

## Project Structure

```text
agentkit/
├── src/agentkit/
│   ├── engine/
│   ├── skills/
│   ├── cli/
│   ├── connectors/
│   ├── logging_metrics/
│   └── templates/
├── tests/
├── .github/workflows/tests.yml
├── Dockerfile
└── pyproject.toml
```

## Quickstart

```bash
pip install -e .
python -m pytest
```

## CLI Usage

```bash
agentkit scaffold ./my-agent
agentkit skill-template customer-support
agentkit metrics stars_received
```

## License

MIT
