from pydantic import BaseModel, Field


# -----------------------------
# Summary
# -----------------------------
class IntegrationSummary(BaseModel):
    connected: int
    available: int
    healthy: int
    sync_rate: str


# -----------------------------
# Integration
# -----------------------------
class IntegrationItem(BaseModel):
    name: str
    category: str
    status: str


# -----------------------------
# AI Recommendation
# -----------------------------
class AIRecommendation(BaseModel):
    title: str
    description: str


# -----------------------------
# Response
# -----------------------------
class IntegrationsSummary(BaseModel):
    summary: IntegrationSummary

    integrations: list[IntegrationItem] = Field(default_factory=list)

    ai_recommendation: AIRecommendation