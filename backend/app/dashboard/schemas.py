from pydantic import BaseModel, Field


# -----------------------------
# Dashboard Cards
# -----------------------------
class DashboardCards(BaseModel):
    connected_clouds: int = Field(default=0)
    platform_health: float = Field(default=100.0)
    active_incidents: int = Field(default=0)
    ai_confidence: int = Field(default=95)


# -----------------------------
# Priority Feed
# -----------------------------
class PriorityItem(BaseModel):
    severity: str
    title: str
    description: str


# -----------------------------
# Recent Activity
# -----------------------------
class ActivityItem(BaseModel):
    title: str
    timestamp: str


# -----------------------------
# AI Insights
# -----------------------------
class AIInsight(BaseModel):
    title: str
    description: str


# -----------------------------
# Dashboard Response
# -----------------------------
class DashboardSummary(BaseModel):
    cards: DashboardCards

    priority_feed: list[PriorityItem] = Field(default_factory=list)
    recent_activity: list[ActivityItem] = Field(default_factory=list)
    ai_insights: list[AIInsight] = Field(default_factory=list)