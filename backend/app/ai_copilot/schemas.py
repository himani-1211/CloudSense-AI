from pydantic import BaseModel, Field


# -----------------------------
# Suggested Questions
# -----------------------------
class SuggestedQuestion(BaseModel):
    text: str


# -----------------------------
# Chat Messages
# -----------------------------
class ChatMessage(BaseModel):
    role: str
    text: str
    timestamp: str


# -----------------------------
# AI Recommendation
# -----------------------------
class AIRecommendation(BaseModel):
    actions: list[str] = Field(default_factory=list)


# -----------------------------
# AI Response
# -----------------------------
class AIResponse(BaseModel):
    message: str
    recommendation: AIRecommendation


# -----------------------------
# AI Capabilities
# -----------------------------
class Capability(BaseModel):
    title: str
    description: str


# -----------------------------
# Copilot Summary Response
# -----------------------------
class CopilotSummary(BaseModel):
    suggested_questions: list[SuggestedQuestion] = Field(default_factory=list)

    conversation: list[ChatMessage] = Field(default_factory=list)

    response: AIResponse

    capabilities: list[Capability] = Field(default_factory=list)


# =====================================================
# Chat API Schemas
# =====================================================

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = Field(default_factory=list)