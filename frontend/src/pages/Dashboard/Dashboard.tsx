import { useEffect, useState } from "react";

import DashboardLayout from "../../layouts/DashboardLayout";
import Hero from "../../components/dashboard/Hero";
import KPISection from "../../components/dashboard/KPISection";

import { getDashboardSummary } from "../../api/dashboard";
import type { DashboardSummary } from "../../api/dashboard";

export default function Dashboard() {
  const [dashboard, setDashboard] =
    useState<DashboardSummary | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const data = await getDashboardSummary();
        setDashboard(data);
      } catch (error) {
        console.error("Failed to load dashboard:", error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="py-20 text-center text-slate-400">
          Loading dashboard...
        </div>
      </DashboardLayout>
    );
  }

  if (!dashboard) {
    return (
      <DashboardLayout>
        <div className="py-20 text-center text-red-400">
          Failed to load dashboard.
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <Hero cards={dashboard.cards} />

      <KPISection
        priorityFeed={dashboard.priority_feed}
        recentActivity={dashboard.recent_activity}
        aiInsights={dashboard.ai_insights}
      />
    </DashboardLayout>
  );
}