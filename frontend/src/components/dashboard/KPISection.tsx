import {
  AlertTriangle,
  ArrowRight,
  BrainCircuit,
  Clock3,
} from "lucide-react";

import type {
  ActivityItem as Activity,
  AIInsight,
  PriorityItem,
} from "../../api/dashboard";

interface KPISectionProps {
  priorityFeed: PriorityItem[];
  recentActivity: Activity[];
  aiInsights: AIInsight[];
}

export default function KPISection({
  priorityFeed,
  recentActivity,
  aiInsights,
}: KPISectionProps) {
  return (
    <section className="space-y-8">
      {/* Top Grid */}
      <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">
        {/* Priority Feed */}
        <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-[#151C31] p-6">
          <div className="mb-6 flex items-center justify-between">
            <div>
              <h2 className="text-xl font-semibold text-white">
                Priority Feed
              </h2>

              <p className="mt-1 text-sm text-slate-400">
                AI-ranked operational events requiring your attention.
              </p>
            </div>
          </div>

          <div className="space-y-4">
            {priorityFeed.length > 0 ? (
              priorityFeed.map((item, index) => (
                <PriorityCard
                  key={index}
                  color={getPriorityColor(item.severity)}
                  title={item.title}
                  description={item.description}
                />
              ))
            ) : (
              <p className="text-sm text-slate-400">
                No priority events.
              </p>
            )}
          </div>
        </div>

        {/* Activity */}
        <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
          <h2 className="text-xl font-semibold text-white">
            Recent Activity
          </h2>

          <p className="mt-1 text-sm text-slate-400">
            Latest platform events.
          </p>

          <div className="mt-6 space-y-5">
            {recentActivity.length > 0 ? (
              recentActivity.map((activity, index) => (
                <ActivityCard
                  key={index}
                  title={activity.title}
                  time={activity.timestamp}
                />
              ))
            ) : (
              <p className="text-sm text-slate-400">
                No recent activity.
              </p>
            )}
          </div>
        </div>
      </div>

      {/* AI Insights */}
      <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h2 className="text-xl font-semibold text-white">
              Recent AI Insights
            </h2>

            <p className="mt-1 text-sm text-slate-400">
              Intelligent recommendations generated from your cloud environment.
            </p>
          </div>

          <button className="flex items-center gap-2 text-cyan-400 transition hover:text-cyan-300">
            View all
            <ArrowRight size={16} />
          </button>
        </div>

        <div className="grid grid-cols-1 gap-5 lg:grid-cols-3">
          {aiInsights.length > 0 ? (
            aiInsights.map((insight, index) => (
              <InsightCard
                key={index}
                title={insight.title}
                description={insight.description}
              />
            ))
          ) : (
            <p className="text-sm text-slate-400">
              No AI insights available.
            </p>
          )}
        </div>
      </div>
    </section>
  );
}

function getPriorityColor(
  severity: string
): "red" | "yellow" | "blue" {
  switch (severity.toLowerCase()) {
    case "critical":
    case "high":
      return "red";

    case "warning":
    case "medium":
      return "yellow";

    default:
      return "blue";
  }
}

interface PriorityCardProps {
  title: string;
  description: string;
  color: "red" | "yellow" | "blue";
}

function PriorityCard({
  title,
  description,
  color,
}: PriorityCardProps) {
  const colors = {
    red: "bg-red-500/10 text-red-400",
    yellow: "bg-yellow-500/10 text-yellow-400",
    blue: "bg-cyan-500/10 text-cyan-400",
  };

  return (
    <div className="flex items-start justify-between rounded-2xl border border-white/10 p-5 transition hover:border-cyan-500/20">
      <div className="flex gap-4">
        <div className={`rounded-xl p-3 ${colors[color]}`}>
          <AlertTriangle size={18} />
        </div>

        <div>
          <h3 className="font-semibold text-white">
            {title}
          </h3>

          <p className="mt-2 text-sm text-slate-400">
            {description}
          </p>
        </div>
      </div>

      <ArrowRight
        className="text-slate-500"
        size={18}
      />
    </div>
  );
}

function ActivityCard({
  title,
  time,
}: {
  title: string;
  time: string;
}) {
  return (
    <div className="flex gap-3">
      <Clock3
        size={16}
        className="mt-1 text-cyan-400"
      />

      <div>
        <p className="text-sm text-white">
          {title}
        </p>

        <p className="text-xs text-slate-500">
          {time}
        </p>
      </div>
    </div>
  );
}

function InsightCard({
  title,
  description,
}: {
  title: string;
  description: string;
}) {
  return (
    <div className="rounded-2xl border border-white/10 p-5 transition hover:border-cyan-500/20">
      <div className="mb-4 inline-flex rounded-xl bg-cyan-500/10 p-3 text-cyan-400">
        <BrainCircuit size={20} />
      </div>

      <h3 className="font-semibold text-white">
        {title}
      </h3>

      <p className="mt-2 text-sm leading-6 text-slate-400">
        {description}
      </p>
    </div>
  );
}