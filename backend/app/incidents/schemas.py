from pydantic import BaseModel, Field


# -----------------------------
# Summary Cards
# -----------------------------
class IncidentSummary(BaseModel):
    open: int
    critical: int
    resolved_today: int
    average_resolution: str


# -----------------------------
# Incident List
# -----------------------------
class IncidentItem(BaseModel):
    severity: str
    title: str
    service: str
    status: str
    time: str


# -----------------------------
# Current Priority
# -----------------------------
class CurrentPriority(BaseModel):
    title: str
    description: str
    impact: str
    impact_description: str


# -----------------------------
# Response
# -----------------------------
class IncidentsSummary(BaseModel):
    summary: IncidentSummary

    incidents: list[IncidentItem] = Field(default_factory=list)

    current_priority: CurrentPriority