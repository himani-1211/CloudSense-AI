from pydantic import BaseModel, Field


# -----------------------------
# Report Statistics
# -----------------------------
class ReportStatistics(BaseModel):
    reports_generated: int
    performance_score: str
    compliance: str
    average_report_time: str


# -----------------------------
# Recent Report
# -----------------------------
class ReportItem(BaseModel):
    title: str
    category: str
    date: str


# -----------------------------
# AI Insight
# -----------------------------
class ReportInsight(BaseModel):
    title: str
    description: str


# -----------------------------
# Response
# -----------------------------
class ReportsSummary(BaseModel):
    statistics: ReportStatistics

    recent_reports: list[ReportItem] = Field(default_factory=list)

    ai_insight: ReportInsight