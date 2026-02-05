"""Claude-style skills compatibility layer and manifest helpers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class SkillManifest:
    name: str
    version: str
    entrypoint: str
    description: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SkillManifest":
        required = {"name", "version", "entrypoint", "description"}
        missing = required - set(data)
        if missing:
            missing_str = ", ".join(sorted(missing))
            raise ValueError(f"Missing required manifest fields: {missing_str}")
        return cls(
            name=str(data["name"]),
            version=str(data["version"]),
            entrypoint=str(data["entrypoint"]),
            description=str(data["description"]),
        )


def load_manifest(path: str | Path) -> SkillManifest:
    manifest_data = json.loads(Path(path).read_text(encoding="utf-8"))
    return SkillManifest.from_dict(manifest_data)


def render_skill_template(name: str) -> dict[str, Any]:
    return {
        "name": name,
        "version": "0.1.0",
        "entrypoint": f"skills.{name}.main:run",
        "description": f"{name} skill template",
    }
