import api from "./axios";

export interface ReportStatistics {
  reports_generated: number;
  performance_score: string;
  compliance: string;
  average_report_time: string;
}

export interface ReportItem {
  title: string;
  category: string;
  date: string;
}

export interface ReportInsight {
  title: string;
  description: string;
}

export interface ReportsSummary {
  statistics: ReportStatistics;
  recent_reports: ReportItem[];
  ai_insight: ReportInsight;
}

export async function getReportsSummary(): Promise<ReportsSummary> {
  const response = await api.get<ReportsSummary>("/reports/summary");
  return response.data;
}