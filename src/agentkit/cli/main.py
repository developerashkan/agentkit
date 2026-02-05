"""CLI developer toolkit for scaffolding and basic evaluation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from agentkit.logging_metrics.metrics import MetricsCollector
from agentkit.skills.compat import render_skill_template


def scaffold_project(path: str) -> Path:
    root = Path(path)
    root.mkdir(parents=True, exist_ok=True)
    (root / "agents").mkdir(exist_ok=True)
    (root / "skills").mkdir(exist_ok=True)
    (root / "connectors").mkdir(exist_ok=True)
    (root / "README.md").write_text("# New Agent Project\n", encoding="utf-8")
    return root


def command_skill_template(name: str) -> str:
    return json.dumps(render_skill_template(name), indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(prog="agentkit")
    sub = parser.add_subparsers(dest="command", required=True)

    scaffold = sub.add_parser("scaffold", help="Scaffold a new agent project")
    scaffold.add_argument("path")

    skill = sub.add_parser("skill-template", help="Generate skill manifest template")
    skill.add_argument("name")

    metrics = sub.add_parser("metrics", help="Record a usage event")
    metrics.add_argument("event")

    args = parser.parse_args()

    if args.command == "scaffold":
        root = scaffold_project(args.path)
        print(f"Scaffolded project at {root}")
    elif args.command == "skill-template":
        print(command_skill_template(args.name))
    elif args.command == "metrics":
        collector = MetricsCollector()
        collector.record(args.event)
        print(collector.summary())


if __name__ == "__main__":
    main()
