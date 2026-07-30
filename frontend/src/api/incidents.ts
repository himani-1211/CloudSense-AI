import api from "./axios";

export interface IncidentSummary {
  open: number;
  critical: number;
  resolved_today: number;
  average_resolution: string;
}

export interface IncidentItem {
  severity: string;
  title: string;
  service: string;
  status: string;
  time: string;
}

export interface CurrentPriority {
  title: string;
  description: string;
  impact: string;
  impact_description: string;
}

export interface IncidentsSummary {
  summary: IncidentSummary;
  incidents: IncidentItem[];
  current_priority: CurrentPriority;
}

export async function getIncidentsSummary(): Promise<IncidentsSummary> {
  const response = await api.get<IncidentsSummary>("/incidents/summary");
  return response.data;
}