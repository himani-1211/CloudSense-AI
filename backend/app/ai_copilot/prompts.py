from textwrap import dedent

from app.ai_copilot.rag.retriever import RetrievedChunk

SYSTEM_PROMPT = dedent("""
You are CloudSense AI, an AI Cloud Engineer embedded inside the CloudSense AI platform.

You have two sources of information, both supplied to you below:

1. KNOWLEDGE — retrieved reference material about cloud services and best practices, which may
   cover AWS, Azure, GCP, Oracle Cloud, or cross-cloud concepts.
2. INFRASTRUCTURE — the user's actual, live cloud resources.

Rules:

1. Ground your answer in the supplied KNOWLEDGE and INFRASTRUCTURE. Do not invent resources,
   counts, or facts that aren't present in them.
2. When KNOWLEDGE and INFRASTRUCTURE are both relevant, connect them explicitly - explain what the
   concept means AND what it implies for the user's actual environment.
3. If the supplied information is insufficient to fully answer, say so plainly rather than
   guessing.
4. Keep responses concise, precise, and professional - the tone of a senior cloud engineer, not a
   generic chatbot.
5. When appropriate, end with a concrete, actionable recommendation rather than only description.
6. You do not currently take actions on the user's infrastructure. If asked to perform a change
   (e.g. "stop this instance", "delete this bucket"), explain that you can currently advise and
   explain, and that direct action support is planned for a future release requiring explicit
   user approval.
""").strip()


def build_infrastructure_context(resources: dict) -> str:
    """
    Formats the user's live resources into a compact, LLM-friendly summary.
    Includes resource names (not just counts) so the model can ground
    answers in specifics, capped per category to keep the prompt bounded.
    """

    sections = []

    labels = {
        "ec2": "EC2 Instances",
        "s3": "S3 Buckets",
        "rds": "RDS Databases",
        "lambda": "Lambda Functions",
        "ebs": "EBS Volumes",
        "vpcs": "VPCs",
    }

    for key, label in labels.items():
        items = resources.get(key, [])

        if not items:
            sections.append(f"{label}: none")
            continue

        names = [
            item.get("name") or item.get("id") or "unnamed"
            for item in items[:15]
        ]

        suffix = f", and {len(items) - 15} more" if len(items) > 15 else ""

        sections.append(f"{label} ({len(items)}): {', '.join(names)}{suffix}")

    return "Live Cloud Infrastructure (AWS)\n\n" + "\n".join(sections)


def build_knowledge_context(chunks: list[RetrievedChunk]) -> str:

    if not chunks:
        return "No relevant knowledge base articles were retrieved for this question."

    sections = []

    for chunk in chunks:
        sections.append(
            f"[{chunk.provider.upper()}] {chunk.title}\n{chunk.text}"
        )

    return "\n\n---\n\n".join(sections)


def build_prompt(
    user_message: str,
    infrastructure_context: str,
    knowledge_chunks: list[RetrievedChunk],
) -> str:
    """
    Combines the system prompt, retrieved knowledge, live infrastructure
    context, and the user's question into the final RAG prompt sent to the
    LLM.
    """

    return dedent(
        f"""
        {SYSTEM_PROMPT}

        -------------------------
        KNOWLEDGE
        -------------------------

        {build_knowledge_context(knowledge_chunks)}

        -------------------------
        INFRASTRUCTURE
        -------------------------

        {infrastructure_context}

        -------------------------
        USER QUESTION
        -------------------------

        {user_message}
        """
    ).strip()
