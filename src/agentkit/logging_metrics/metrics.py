"""Real-time logging and usage metrics primitives."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field


@dataclass
class MetricsCollector:
    events: Counter[str] = field(default_factory=Counter)

    def record(self, event: str) -> None:
        self.events[event] += 1

    def summary(self) -> dict[str, int]:
        return dict(self.events)
