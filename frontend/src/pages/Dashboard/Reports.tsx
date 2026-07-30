import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import { getReportsSummary } from "../../api/reports";
import type { ReportsSummary } from "../../api/reports";
import {
  FileBarChart2,
  Download,
  Calendar,
  TrendingUp,
  ShieldCheck,
  Clock3,
  ArrowRight,
} from "lucide-react";

export default function Reports() {
  const [data, setData] = useState<ReportsSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const response = await getReportsSummary();
        setData(response);
      } catch (err) {
        console.error(err);
        setError("Failed to load reports.");
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex h-[60vh] items-center justify-center text-slate-400">
          Loading reports...
        </div>
      </DashboardLayout>
    );
  }

  if (error || !data) {
    return (
      <DashboardLayout>
        <div className="flex h-[60vh] items-center justify-center text-red-400">
          {error || "No reports available."}
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1
              className="text-4xl font-bold text-white"
              style={{ fontFamily: "var(--font-heading)" }}
            >
              Reports
            </h1>

            <p className="mt-2 text-slate-400">
              Generate operational intelligence reports and analyze cloud
              performance trends.
            </p>
          </div>

          <button className="flex items-center gap-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 px-5 py-3 text-white">
            <Download size={18} />
            Export Report
          </button>
        </div>

        {/* Report Cards */}
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
          <StatCard
            icon={<FileBarChart2 size={22} />}
            title="Reports Generated"
            value={String(data.statistics.reports_generated)}
          />

          <StatCard
            icon={<TrendingUp size={22} />}
            title="Performance Score"
            value={data.statistics.performance_score}
          />

          <StatCard
            icon={<ShieldCheck size={22} />}
            title="Compliance"
            value={data.statistics.compliance}
          />

          <StatCard
            icon={<Clock3 size={22} />}
            title="Avg. Report Time"
            value={data.statistics.average_report_time}
          />
        </div>

        {/* Recent Reports */}
        <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
          <h2 className="mb-6 text-xl font-semibold text-white">
            Recent Reports
          </h2>

          <div className="space-y-4">
            {data.recent_reports.length === 0 ? (
              <div className="rounded-2xl border border-white/10 p-8 text-center text-slate-400">
                No reports available.
              </div>
            ) : (
              data.recent_reports.map((report, index) => (
                <ReportItem
                  key={index}
                  title={report.title}
                  type={report.category}
                  date={report.date}
                />
              ))
            )}
          </div>
        </div>

        {/* AI Insights */}
        <div className="rounded-3xl border border-cyan-500/20 bg-gradient-to-r from-cyan-500/10 via-blue-500/10 to-violet-500/10 p-6">
          <div className="flex items-start gap-5">
            <div className="rounded-2xl bg-cyan-500/10 p-4 text-cyan-400">
              <TrendingUp size={28} />
            </div>

            <div>
              <h2 className="text-xl font-semibold text-white">
                {data.ai_insight.title}
              </h2>

              <p className="mt-3 leading-7 text-slate-300">
                {data.ai_insight.description}
              </p>
            </div>
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

function StatCard({
  icon,
  title,
  value,
}: {
  icon: React.ReactNode;
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6">
      <div className="mb-4 inline-flex rounded-xl bg-cyan-500/10 p-3 text-cyan-400">
        {icon}
      </div>

      <p className="text-xs uppercase tracking-[0.18em] text-slate-500">
        {title}
      </p>

      <h3 className="mt-2 text-3xl font-bold text-white">
        {value}
      </h3>
    </div>
  );
}

function ReportItem({
  title,
  type,
  date,
}: {
  title: string;
  type: string;
  date: string;
}) {
  return (
    <div className="flex items-center justify-between rounded-2xl border border-white/10 p-5 transition hover:border-cyan-500/20">
      <div>
        <h3 className="font-semibold text-white">{title}</h3>

        <div className="mt-2 flex items-center gap-5 text-sm text-slate-400">
          <span>{type}</span>

          <div className="flex items-center gap-2">
            <Calendar size={14} />
            {date}
          </div>
        </div>
      </div>

      <ArrowRight className="text-slate-500" size={18} />
    </div>
  );
}