"""Core agent engine with orchestration and async concurrency support."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Iterable

TaskHandler = Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]


@dataclass(slots=True)
class Task:
    """A unit of work passed into the agent orchestration loop."""

    name: str
    payload: dict[str, Any]


class AgentRunner:
    """Modular async runner for executing task handlers concurrently."""

    def __init__(self, max_concurrency: int = 10) -> None:
        self._handlers: dict[str, TaskHandler] = {}
        self._semaphore = asyncio.Semaphore(max_concurrency)

    def register_handler(self, task_name: str, handler: TaskHandler) -> None:
        self._handlers[task_name] = handler

    async def _run_single(self, task: Task) -> dict[str, Any]:
        if task.name not in self._handlers:
            raise KeyError(f"No handler registered for task '{task.name}'")
        async with self._semaphore:
            result = await self._handlers[task.name](task.payload)
            return {"task": task.name, "result": result}

    async def run(self, tasks: Iterable[Task]) -> list[dict[str, Any]]:
        coroutines = [self._run_single(task) for task in tasks]
        return await asyncio.gather(*coroutines)
