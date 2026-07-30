import api from "./axios";

export interface InfrastructureOverview {
  cloud_providers: number;
  compute_instances: number;
  databases: number;
  storage_buckets: number;
}

export interface InfrastructureResource {
  title: string;
  type: string;
  status: string;
  utilization: string;
  uptime: string;
}

export interface InfrastructureHealth {
  overall_health: number;
  average_cpu_usage: number;
  ai_recommendation: string;
}

export interface InfrastructureSummary {
  overview: InfrastructureOverview;
  resources: InfrastructureResource[];
  health: InfrastructureHealth;
}

export async function getInfrastructureSummary() {
  const response = await api.get<InfrastructureSummary>(
    "/infrastructure/summary"
  );

  return response.data;
}