import api from "./axios";

export interface DashboardCards {
  connected_clouds: number;
  platform_health: number;
  active_incidents: number;
  ai_confidence: number;
}

export interface PriorityItem {
  severity: string;
  title: string;
  description: string;
}

export interface ActivityItem {
  title: string;
  timestamp: string;
}

export interface AIInsight {
  title: string;
  description: string;
}

export interface DashboardSummary {
  cards: DashboardCards;
  priority_feed: PriorityItem[];
  recent_activity: ActivityItem[];
  ai_insights: AIInsight[];
}

export async function getDashboardSummary() {
  const response = await api.get<DashboardSummary>(
    "/dashboard/summary"
  );

  return response.data;
}