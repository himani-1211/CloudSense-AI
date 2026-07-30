import api from "./axios";

export interface SettingItem {
  title: string;
  description: string;
}

export interface WorkspaceStatus {
  workspace: string;
  ai_services: string;
  connected_clouds: string;
}

export interface SettingsSummary {
  sections: SettingItem[];
  workspace_status: WorkspaceStatus;
}

export async function getSettingsSummary() {
  const response = await api.get<SettingsSummary>("/settings/summary");
  return response.data;
}