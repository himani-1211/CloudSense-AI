import api from "./axios";

export interface IntegrationSummary {
  connected: number;
  available: number;
  healthy: number;
  sync_rate: string;
}

export interface IntegrationItem {
  name: string;
  category: string;
  status: string;
}

export interface AIRecommendation {
  title: string;
  description: string;
}

export interface IntegrationsSummary {
  summary: IntegrationSummary;
  integrations: IntegrationItem[];
  ai_recommendation: AIRecommendation;
}

export async function getIntegrationsSummary(): Promise<IntegrationsSummary> {
  const response = await api.get<IntegrationsSummary>("/integrations/summary");
  return response.data;
}