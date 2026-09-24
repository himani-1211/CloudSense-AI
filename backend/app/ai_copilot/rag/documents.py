import os
from dataclasses import dataclass, field
from pathlib import Path

KNOWLEDGE_BASE_DIR = Path(__file__).resolve().parent.parent / "knowledge_base"


@dataclass
class Document:
    id: str
    title: str
    provider: str
    category: str
    content: str
    source_path: str


def _parse_frontmatter(raw_text: str) -> tuple[dict, str]:
    """
    Parses a minimal '---\\nkey: value\\n---\\nbody' header, used instead of
    a full YAML parser since knowledge base docs only ever use flat string
    fields.
    """

    lines = raw_text.strip().splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, raw_text.strip()

    metadata: dict = {}
    body_start = len(lines)

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body_start = index + 1
            break

        if ":" in line:
            key, _, value = line.partition(":")
            metadata[key.strip()] = value.strip()

    body = "\n".join(lines[body_start:]).strip()

    return metadata, body


def load_documents(base_dir: Path = KNOWLEDGE_BASE_DIR) -> list[Document]:
    """
    Loads every markdown document in the knowledge base directory tree.

    Provider defaults to the immediate parent folder name (aws/azure/gcp/
    oracle/cross_cloud) when not explicitly set in frontmatter, so new
    providers only need a new folder.
    """

    documents: list[Document] = []

    if not base_dir.exists():
        return documents

    for file_path in sorted(base_dir.rglob("*.md")):

        raw_text = file_path.read_text(encoding="utf-8")
        metadata, body = _parse_frontmatter(raw_text)

        if not body:
            continue

        relative_path = file_path.relative_to(base_dir)
        default_provider = relative_path.parts[0] if len(relative_path.parts) > 1 else "unknown"

        documents.append(
            Document(
                id=str(relative_path).replace(os.sep, "/"),
                title=metadata.get("title", file_path.stem.replace("-", " ").title()),
                provider=metadata.get("provider", default_provider),
                category=metadata.get("category", "general"),
                content=body,
                source_path=str(relative_path).replace(os.sep, "/"),
            )
        )

    return documents
