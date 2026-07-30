import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import {
  BrainCircuit,
  Clock3,
  Filter,
  Search,
  ShieldAlert,
  ServerCrash,
  ArrowRight,
  CircleCheck,
} from "lucide-react";

import {
  getOperationsSummary,
  type OperationsSummary,
} from "../../api/operations";

export default function Operations() {
  const [data, setData] = useState<OperationsSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    (async () => {
      try {
        setData(await getOperationsSummary());
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const timeline = useMemo(() => {
    if (!data) return [];

    return data.timeline.filter((item) =>
      (
        item.title +
        item.description +
        item.severity
      )
        .toLowerCase()
        .includes(search.toLowerCase())
    );
  }, [data, search]);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="py-24 text-center text-slate-400">
          Loading operations...
        </div>
      </DashboardLayout>
    );
  }

  if (!data) {
    return (
      <DashboardLayout>
        <div className="py-24 text-center text-red-400">
          Failed to load operations.
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
              Operations
            </h1>

            <p className="mt-2 text-slate-400">
              Monitor operational events, investigate incidents and let AI
              prioritize what requires immediate attention.
            </p>
          </div>

          <button className="flex items-center gap-2 rounded-xl border border-cyan-500/20 bg-cyan-500/10 px-5 py-3 text-cyan-300 transition hover:bg-cyan-500/20">
            <Filter size={18} />
            Filters
          </button>
        </div>

        {/* AI Summary */}
        <div className="rounded-3xl border border-cyan-500/20 bg-gradient-to-r from-cyan-500/10 via-blue-500/10 to-violet-500/10 p-6">
          <div className="flex items-start gap-5">
            <div className="rounded-2xl bg-cyan-500/15 p-4 text-cyan-400">
              <BrainCircuit size={28} />
            </div>

            <div className="flex-1">
              <h2 className="text-xl font-semibold text-white">
                AI Operations Summary
              </h2>

              <div className="mt-5 grid grid-cols-1 gap-4 md:grid-cols-3">
                <div className="rounded-xl border border-white/10 bg-[#151C31] p-4">
                  <p className="text-xs uppercase tracking-wide text-slate-400">
                    Events Analyzed
                  </p>

                  <h3 className="mt-2 text-3xl font-bold text-white">
                    {data.ai_summary.events_analyzed}
                  </h3>
                </div>

                <div className="rounded-xl border border-white/10 bg-[#151C31] p-4">
                  <p className="text-xs uppercase tracking-wide text-slate-400">
                    Critical Events
                  </p>

                  <h3 className="mt-2 text-3xl font-bold text-red-400">
                    {data.ai_summary.critical_events}
                  </h3>
                </div>

                <div className="rounded-xl border border-white/10 bg-[#151C31] p-4">
                  <p className="text-xs uppercase tracking-wide text-slate-400">
                    Performance Risks
                  </p>

                  <h3 className="mt-2 text-3xl font-bold text-yellow-400">
                    {data.ai_summary.performance_risks}
                  </h3>
                </div>
              </div>

              <p className="mt-5 max-w-4xl leading-7 text-slate-300">
                {data.ai_summary.summary}
              </p>
            </div>
          </div>
        </div>

        {/* Search */}
        <div className="flex h-12 items-center gap-3 rounded-2xl border border-white/10 bg-[#151C31] px-4">
          <Search
            size={18}
            className="text-slate-400"
          />

          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search operations..."
            className="w-full bg-transparent text-white outline-none placeholder:text-slate-500"
          />
        </div>
        <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">
          {/* Timeline */}
          <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-[#151C31] p-6">
            <h2 className="mb-6 text-xl font-semibold text-white">
              Operations Timeline
            </h2>

            <div className="space-y-5">
              {timeline.length === 0 ? (
                <div className="py-8 text-center text-slate-400">
                  No operational events found.
                </div>
              ) : (
                timeline.map((item, index) => (
                  <TimelineItem
                    key={index}
                    icon={
                      item.severity === "healthy" ? (
                        <CircleCheck size={18} />
                      ) : item.severity === "warning" ? (
                        <ShieldAlert size={18} />
                      ) : (
                        <ServerCrash size={18} />
                      )
                    }
                    title={item.title}
                    description={item.description}
                    time={item.time}
                    color={
                      item.severity === "healthy"
                        ? "green"
                        : item.severity === "warning"
                        ? "yellow"
                        : "red"
                    }
                  />
                ))
              )}
            </div>
          </div>

          {/* AI Correlation */}
          <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
            <h2 className="text-xl font-semibold text-white">
              AI Correlation
            </h2>

            <div className="mt-6 rounded-2xl bg-cyan-500/10 p-5">
              <p className="text-xs uppercase tracking-[0.2em] text-cyan-400">
                Root Cause
              </p>

              <p className="mt-3 text-white">
                {data.ai_correlation.root_cause}
              </p>
            </div>

            <div className="mt-5 rounded-2xl border border-white/10 p-5">
              <p className="text-xs uppercase tracking-[0.2em] text-slate-500">
                AI Confidence
              </p>

              <h3 className="mt-2 text-4xl font-bold text-white">
                {data.ai_correlation.confidence}%
              </h3>

              <p className="mt-3 text-sm text-slate-400">
                {data.ai_correlation.analysis}
              </p>
            </div>

            <button className="mt-6 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 px-4 py-3 font-medium text-white transition hover:opacity-90">
              View Full Analysis
              <ArrowRight size={18} />
            </button>
          </div>
        </div>

        {/* Recommended Actions */}
        <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
          <h2 className="mb-6 text-xl font-semibold text-white">
            Recommended Actions
          </h2>

          <div className="space-y-4">
            {data.recommended_actions.length === 0 ? (
              <div className="py-6 text-center text-slate-400">
                No recommendations available.
              </div>
            ) : (
              data.recommended_actions.map((action, index) => (
                <ActionCard key={index} text={action.text} />
              ))
            )}
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

interface TimelineItemProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  time: string;
  color: "red" | "yellow" | "green";
}

function TimelineItem({
  icon,
  title,
  description,
  time,
  color,
}: TimelineItemProps) {
  const colors = {
    red: "bg-red-500/10 text-red-400",
    yellow: "bg-yellow-500/10 text-yellow-400",
    green: "bg-emerald-500/10 text-emerald-400",
  };

  return (
    <div className="flex items-start gap-4 rounded-2xl border border-white/10 p-5">
      <div className={`rounded-xl p-3 ${colors[color]}`}>
        {icon}
      </div>

      <div className="flex-1">
        <h3 className="font-semibold text-white">
          {title}
        </h3>

        <p className="mt-2 text-sm text-slate-400">
          {description}
        </p>
      </div>

      <div className="flex items-center gap-2 text-xs text-slate-500">
        <Clock3 size={14} />
        {time}
      </div>
    </div>
  );
}

function ActionCard({ text }: { text: string }) {
  return (
    <div className="flex items-center justify-between rounded-2xl border border-white/10 p-5 transition hover:border-cyan-500/20">
      <p className="text-white">
        {text}
      </p>

      <ArrowRight
        size={18}
        className="text-cyan-400"
      />
    </div>
  );
}