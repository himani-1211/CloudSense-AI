import {
  CheckCircle2,
  BrainCircuit,
  AlertTriangle,
  Cloud,
  Sparkles,
} from "lucide-react";

import type { DashboardCards } from "../../api/dashboard";

interface HeroProps {
  cards: DashboardCards;
}

export default function Hero({ cards }: HeroProps) {
  return (
    <section className="mb-10">
      {/* Header */}
      <div className="mb-8">
        <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-cyan-500/20 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
          <Sparkles size={16} />
          AI-Powered Multi-Cloud Operations Intelligence
        </div>

        <h1
          className="text-5xl font-bold tracking-tight text-white"
          style={{ fontFamily: "var(--font-heading)" }}
        >
          Welcome back,
          <span className="bg-gradient-to-r from-cyan-400 via-blue-500 to-violet-500 bg-clip-text text-transparent">
            {" "}Himani 👋
          </span>
        </h1>

        <p className="mt-5 max-w-3xl text-lg leading-8 text-slate-400">
          Everything happening across your connected cloud ecosystem,
          intelligently analyzed and prioritized by AI.
        </p>
      </div>

      {/* Status Cards */}
      <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4">
        <StatusCard
          icon={<Cloud size={20} />}
          title="Connected Clouds"
          value={cards.connected_clouds.toString()}
          subtitle={
            cards.connected_clouds > 0
              ? "AWS Connected"
              : "No Cloud Connected"
          }
          color="blue"
        />

        <StatusCard
          icon={<CheckCircle2 size={20} />}
          title="Platform Health"
          value={`${cards.platform_health}%`}
          subtitle="Infrastructure Health"
          color="green"
        />

        <StatusCard
          icon={<AlertTriangle size={20} />}
          title="Active Incidents"
          value={cards.active_incidents.toString()}
          subtitle={
            cards.active_incidents > 0
              ? "Requires Attention"
              : "No Active Incidents"
          }
          color="orange"
        />

        <StatusCard
          icon={<BrainCircuit size={20} />}
          title="AI Confidence"
          value={`${cards.ai_confidence}%`}
          subtitle="Live Analysis"
          color="purple"
        />
      </div>
    </section>
  );
}

interface StatusCardProps {
  icon: React.ReactNode;
  title: string;
  value: string;
  subtitle: string;
  color: "blue" | "green" | "orange" | "purple";
}

function StatusCard({
  icon,
  title,
  value,
  subtitle,
  color,
}: StatusCardProps) {
  const colors = {
    blue: "bg-cyan-500/10 text-cyan-400",
    green: "bg-emerald-500/10 text-emerald-400",
    orange: "bg-orange-500/10 text-orange-400",
    purple: "bg-violet-500/10 text-violet-400",
  };

  return (
    <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6 transition-all duration-200 hover:border-cyan-500/20 hover:-translate-y-1">
      <div className={`mb-5 inline-flex rounded-xl p-3 ${colors[color]}`}>
        {icon}
      </div>

      <p className="text-xs uppercase tracking-[0.18em] text-slate-500">
        {title}
      </p>

      <h3 className="mt-2 text-3xl font-bold text-white">{value}</h3>

      <p className="mt-2 text-sm text-slate-400">{subtitle}</p>
    </div>
  );
}