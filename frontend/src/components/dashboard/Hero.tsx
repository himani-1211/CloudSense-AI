import {
  Activity,
  CheckCircle2,
  RefreshCw,
} from "lucide-react";

export default function Hero() {
  return (
    <section className="mb-8 flex items-start justify-between">

      {/* Left */}

      <div>

        <h1
         className="text-5xl font-semibold tracking-tight text-white"
         style={{ fontFamily: "var(--font-heading)" }}
         >
            Cloud Intelligence Dashboard
            </h1>

        <p className="mt-3 max-w-2xl text-base leading-7 text-slate-400">
          Monitor, optimize and secure your cloud infrastructure
          with AI-powered insights and real-time recommendations.
        </p>

      </div>

      {/* Right */}

      <div className="flex gap-4">

        <InfoCard
          icon={<RefreshCw size={18} />}
          title="Last Synced"
          value="2 minutes ago"
        />

        <InfoCard
          icon={<Activity size={18} />}
          title="AWS Region"
          value="us-east-1"
        />

        <InfoCard
          icon={<CheckCircle2 size={18} />}
          title="Health"
          value="Excellent"
          green
        />

      </div>

    </section>
  );
}

interface InfoCardProps {
  icon: React.ReactNode;
  title: string;
  value: string;
  green?: boolean;
}

function InfoCard({
  icon,
  title,
  value,
  green = false,
}: InfoCardProps) {
  return (
    <div className="flex min-w-[170px] items-center gap-4 rounded-2xl border border-white/10 bg-[#151C31] px-5 py-4">

      <div
        className={`rounded-xl p-3 ${
          green
            ? "bg-emerald-500/15 text-emerald-400"
            : "bg-indigo-500/15 text-indigo-400"
        }`}
      >
        {icon}
      </div>

      <div>

        <p className="text-xs uppercase tracking-wider text-slate-500">
          {title}
        </p>

        <p
          className={`mt-1 font-semibold ${
            green ? "text-emerald-400" : "text-white"
          }`}
        >
          {value}
        </p>

      </div>

    </div>
  );
}