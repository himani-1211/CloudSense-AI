from pydantic import BaseModel, Field


# -----------------------------
# AI Summary
# -----------------------------
class AISummary(BaseModel):
    events_analyzed: int
    critical_events: int
    performance_risks: int
    summary: str


# -----------------------------
# Timeline
# -----------------------------
class TimelineItem(BaseModel):
    severity: str
    title: str
    description: str
    time: str


# -----------------------------
# AI Correlation
# -----------------------------
class AICorrelation(BaseModel):
    root_cause: str
    confidence: int
    analysis: str


# -----------------------------
# Recommended Actions
# -----------------------------
class RecommendedAction(BaseModel):
    text: str


# -----------------------------
# Operations Response
# -----------------------------
class OperationsSummary(BaseModel):
    ai_summary: AISummary

    timeline: list[TimelineItem] = Field(default_factory=list)

    ai_correlation: AICorrelation

    recommended_actions: list[RecommendedAction] = Field(
        default_factory=list
    )