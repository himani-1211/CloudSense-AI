import type { ReactNode } from "react";
import { ArrowUpRight, MoreHorizontal } from "lucide-react";

interface KPICardProps {
  title: string;
  value: string;
  trend: string;
  icon: ReactNode;
  iconBg: string;
  iconColor: string;
}

export default function KPICard({
  title,
  value,
  trend,
  icon,
  iconBg,
  iconColor,
}: KPICardProps) {
  return (
    <div
      className="
        group
        rounded-3xl
        border
        border-white/10
        bg-[#151C31]
        p-6
        transition-all
        duration-300
        hover:-translate-y-1
        hover:border-indigo-500/40
        hover:shadow-[0_0_30px_rgba(99,102,241,0.12)]
      "
    >
      {/* Top */}

      <div className="flex items-start justify-between">
        <div
          className="flex h-14 w-14 items-center justify-center rounded-2xl"
          style={{
            backgroundColor: iconBg,
            color: iconColor,
          }}
        >
          {icon}
        </div>

        <button className="text-slate-500 transition hover:text-white">
            <MoreHorizontal size={18} />
        </button>
      </div>

      {/* Content */}

      <div className="mt-6">
        <p className="text-sm text-slate-400">
          {title}
        </p>

        <h2 className="mt-2 text-4xl font-bold text-white">
          {value}
        </h2>

        <div className="mt-3 flex items-center gap-2">
          <ArrowUpRight
            size={16}
            className="text-emerald-400"
          />

          <span className="font-medium text-emerald-400">
            {trend}
          </span>

          <span className="text-sm text-slate-500">
            vs last month
          </span>
        </div>

        {/* Graph Placeholder */}

        <div className="mt-6 h-12 rounded-xl bg-gradient-to-r from-indigo-500/20 via-purple-500/10 to-transparent" />
      </div>
    </div>
  );
}