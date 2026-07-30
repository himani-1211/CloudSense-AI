import api from "./axios";

export interface SuggestedQuestion {
  text: string;
}

export interface ChatMessage {
  role: string;
  text: string;
  timestamp: string;
}

export interface AIRecommendation {
  actions: string[];
}

export interface AIResponse {
  message: string;
  recommendation: AIRecommendation;
}

export interface Capability {
  title: string;
  description: string;
}

export interface CopilotSummary {
  suggested_questions: SuggestedQuestion[];
  conversation: ChatMessage[];
  response: AIResponse;
  capabilities: Capability[];
}

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  answer: string;
  sources: string[];
}

export async function getCopilotSummary(): Promise<CopilotSummary> {
  const response = await api.get("/ai-copilot/summary");
  return response.data;
}

export async function chatWithCopilot(
  message: string
): Promise<ChatResponse> {
  const response = await api.post("/ai-copilot/chat", {
    message,
  });

  return response.data;
}