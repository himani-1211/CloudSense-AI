import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import { getIncidentsSummary } from "../../api/incidents";
import type { IncidentsSummary } from "../../api/incidents";
import {
  AlertTriangle,
  CheckCircle2,
  Clock3,
  Search,
  Filter,
  ArrowRight,
} from "lucide-react";

export default function Incidents() {
  const [data, setData] = useState<IncidentsSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const response = await getIncidentsSummary();
        setData(response);
      } catch (err) {
        console.error(err);
        setError("Failed to load incidents.");
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const filteredIncidents = useMemo(() => {
    if (!data) return [];

    return data.incidents.filter((incident) =>
      `${incident.title} ${incident.service} ${incident.status} ${incident.severity}`
        .toLowerCase()
        .includes(search.toLowerCase())
    );
  }, [data, search]);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex h-[60vh] items-center justify-center text-slate-400">
          Loading incidents...
        </div>
      </DashboardLayout>
    );
  }

  if (error || !data) {
    return (
      <DashboardLayout>
        <div className="flex h-[60vh] items-center justify-center text-red-400">
          {error || "No incident data available."}
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
              Incidents
            </h1>

            <p className="mt-2 text-slate-400">
              Track ongoing incidents, review their impact and monitor
              resolution progress across your cloud environment.
            </p>
          </div>

          <button className="flex items-center gap-2 rounded-xl border border-cyan-500/20 bg-cyan-500/10 px-5 py-3 text-cyan-300 transition hover:bg-cyan-500/20">
            <Filter size={18} />
            Filters
          </button>
        </div>

        {/* Search */}
        <div className="flex h-12 items-center gap-3 rounded-2xl border border-white/10 bg-[#151C31] px-4">
          <Search size={18} className="text-slate-400" />

          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search incidents..."
            className="w-full bg-transparent text-white outline-none placeholder:text-slate-500"
          />
        </div>

        {/* Summary */}
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4">
          <SummaryCard
            title="Open"
            value={String(data.summary.open)}
            color="red"
          />

          <SummaryCard
            title="Critical"
            value={String(data.summary.critical)}
            color="orange"
          />

          <SummaryCard
            title="Resolved Today"
            value={String(data.summary.resolved_today)}
            color="green"
          />

          <SummaryCard
            title="Avg Resolution"
            value={data.summary.average_resolution}
            color="blue"
          />
        </div>

        {/* Main Layout */}
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">
          {/* Incident List */}
          <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-[#151C31] p-6">
            <h2 className="mb-6 text-xl font-semibold text-white">
              Active Incidents
            </h2>

            <div className="space-y-4">
              {filteredIncidents.length === 0 ? (
                <div className="rounded-2xl border border-white/10 p-8 text-center text-slate-400">
                  No incidents found.
                </div>
              ) : (
                filteredIncidents.map((incident, index) => (
                  <IncidentCard
                    key={index}
                    severity={incident.severity}
                    title={incident.title}
                    service={incident.service}
                    status={incident.status}
                    time={incident.time}
                  />
                ))
              )}
            </div>
          </div>

          {/* Details */}
          <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
            <h2 className="text-xl font-semibold text-white">
              Incident Details
            </h2>

            <div className="mt-6 rounded-2xl border border-red-500/20 bg-red-500/10 p-5">
              <p className="text-xs uppercase tracking-[0.2em] text-red-400">
                Current Priority
              </p>

              <h3 className="mt-3 text-xl font-semibold text-white">
                {data.current_priority.title}
              </h3>

              <p className="mt-3 text-sm leading-6 text-slate-300">
                {data.current_priority.description}
              </p>
            </div>

            <div className="mt-5 rounded-2xl border border-white/10 p-5">
              <p className="text-xs uppercase tracking-[0.2em] text-slate-500">
                Estimated Impact
              </p>

              <h3 className="mt-3 text-3xl font-bold text-white">
                {data.current_priority.impact}
              </h3>

              <p className="mt-2 text-sm text-slate-400">
                {data.current_priority.impact_description}
              </p>
            </div>

            <button className="mt-6 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 px-5 py-3 font-medium text-white transition hover:opacity-90">
              View Timeline
              <ArrowRight size={18} />
            </button>
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

interface SummaryCardProps {
  title: string;
  value: string;
  color: "red" | "orange" | "green" | "blue";
}

function SummaryCard({
  title,
  value,
  color,
}: SummaryCardProps) {
  const colors = {
    red: "bg-red-500/10 text-red-400",
    orange: "bg-orange-500/10 text-orange-400",
    green: "bg-emerald-500/10 text-emerald-400",
    blue: "bg-cyan-500/10 text-cyan-400",
  };

  return (
    <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6">
      <div className={`mb-4 inline-flex rounded-xl p-3 ${colors[color]}`}>
        <AlertTriangle size={20} />
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

interface IncidentCardProps {
  severity: string;
  title: string;
  service: string;
  status: string;
  time: string;
}

function IncidentCard({
  severity,
  title,
  service,
  status,
  time,
}: IncidentCardProps) {
  const severityColors: Record<string, string> = {
    Critical: "bg-red-500/10 text-red-400",
    High: "bg-orange-500/10 text-orange-400",
    Medium: "bg-yellow-500/10 text-yellow-400",
    Low: "bg-emerald-500/10 text-emerald-400",
  };

  return (
    <div className="rounded-2xl border border-white/10 p-5 transition hover:border-cyan-500/20">
      <div className="flex items-center justify-between">
        <span
          className={`rounded-full px-3 py-1 text-xs font-medium ${
            severityColors[severity] ?? "bg-slate-500/10 text-slate-400"
          }`}
        >
          {severity}
        </span>

        <div className="flex items-center gap-2 text-xs text-slate-500">
          <Clock3 size={14} />
          {time}
        </div>
      </div>

      <h3 className="mt-4 text-lg font-semibold text-white">
        {title}
      </h3>

      <p className="mt-2 text-sm text-slate-400">
        Service: {service}
      </p>

      <div className="mt-5 flex items-center justify-between">
        <div className="flex items-center gap-2 text-cyan-400">
          <CheckCircle2 size={16} />
          <span className="text-sm">{status}</span>
        </div>

        <ArrowRight size={18} className="text-slate-500" />
      </div>
    </div>
  );
}