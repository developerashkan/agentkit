"""File ingestion and RAG-ready chunking pipeline."""

from __future__ import annotations

from pathlib import Path


def ingest_text_file(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = 300) -> list[str]:
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def rag_ready_documents(path: str | Path, chunk_size: int = 300) -> list[dict[str, str]]:
    text = ingest_text_file(path)
    chunks = chunk_text(text, chunk_size=chunk_size)
    return [{"id": str(i), "content": chunk} for i, chunk in enumerate(chunks)]
