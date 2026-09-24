import json
from dataclasses import asdict
from pathlib import Path

import numpy as np

from app.ai_copilot.rag.chunker import Chunk

INDEX_DIR = Path(__file__).resolve().parent / "index"
VECTORS_PATH = INDEX_DIR / "knowledge_index.npy"
METADATA_PATH = INDEX_DIR / "knowledge_index.json"


class VectorStore:

    def __init__(self, vectors: np.ndarray, chunks: list[Chunk]):
        self.vectors = vectors
        self.chunks = chunks

    def search(self, query_vector: list[float], top_k: int) -> list[tuple[Chunk, float]]:

        if self.vectors.size == 0:
            return []

        query = np.asarray(query_vector, dtype=np.float32)
        query_norm = np.linalg.norm(query)

        if query_norm == 0:
            return []

        query = query / query_norm

        scores = self.vectors @ query

        top_indices = np.argsort(-scores)[:top_k]

        return [(self.chunks[i], float(scores[i])) for i in top_indices]

    def save(self) -> None:
        INDEX_DIR.mkdir(parents=True, exist_ok=True)

        np.save(VECTORS_PATH, self.vectors)

        METADATA_PATH.write_text(
            json.dumps([asdict(chunk) for chunk in self.chunks], indent=2),
            encoding="utf-8",
        )

    @classmethod
    def load(cls) -> "VectorStore | None":

        if not VECTORS_PATH.exists() or not METADATA_PATH.exists():
            return None

        vectors = np.load(VECTORS_PATH)

        raw_chunks = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
        chunks = [Chunk(**item) for item in raw_chunks]

        return cls(vectors=vectors, chunks=chunks)

    @classmethod
    def build(cls, chunks: list[Chunk], embeddings: list[list[float]]) -> "VectorStore":

        vectors = np.asarray(embeddings, dtype=np.float32)

        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        vectors = vectors / norms

        return cls(vectors=vectors, chunks=chunks)
