import api from "./axios";

export interface AISummary {
  events_analyzed: number;
  critical_events: number;
  performance_risks: number;
  summary: string;
}

export interface TimelineItem {
  severity: string;
  title: string;
  description: string;
  time: string;
}

export interface AICorrelation {
  root_cause: string;
  confidence: number;
  analysis: string;
}

export interface RecommendedAction {
  text: string;
}

export interface OperationsSummary {
  ai_summary: AISummary;
  timeline: TimelineItem[];
  ai_correlation: AICorrelation;
  recommended_actions: RecommendedAction[];
}

export async function getOperationsSummary(): Promise<OperationsSummary> {
  const response = await api.get<OperationsSummary>("/operations/summary");
  return response.data;
}