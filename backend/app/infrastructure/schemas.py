from pydantic import BaseModel, Field


# -----------------------------
# Resource Overview
# -----------------------------
class InfrastructureOverview(BaseModel):
    cloud_providers: int
    compute_instances: int
    databases: int
    storage_buckets: int


# -----------------------------
# Infrastructure Resources
# -----------------------------
class InfrastructureResource(BaseModel):
    title: str
    type: str
    status: str
    utilization: str
    uptime: str


# -----------------------------
# Health Panel
# -----------------------------
class InfrastructureHealth(BaseModel):
    overall_health: float
    average_cpu_usage: int
    ai_recommendation: str


# -----------------------------
# Response
# -----------------------------
class InfrastructureSummary(BaseModel):
    overview: InfrastructureOverview

    resources: list[InfrastructureResource] = Field(default_factory=list)

    health: InfrastructureHealth