import {
  LayoutDashboard,
  BrainCircuit,
  Cloud,
  BarChart3,
  Shield,
  FileText,
  Plug,
  Settings,
} from "lucide-react";

const menu = [
  { icon: LayoutDashboard, label: "Dashboard" },
  { icon: BrainCircuit, label: "AI Insights" },
  { icon: Cloud, label: "Cloud Resources" },
  { icon: BarChart3, label: "Cost Analytics" },
  { icon: Shield, label: "Security Center" },
  { icon: FileText, label: "Reports" },
  { icon: Plug, label: "Integrations" },
  { icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-[280px] rounded-3xl bg-[#111827] border border-white/10 p-6">

      <div className="mb-10">
        <h1 className="text-[38px] font-bold leading-none text-white"
        style={{ fontFamily: "var(--font-heading)" }}
        >
          CloudSense AI
        </h1>

        <p className="text-sm text-slate-400">
          Cloud Intelligence Platform
        </p>
      </div>

      <nav className="space-y-2">
        {menu.map(({ icon: Icon, label }, index) => (
          <button
            key={label}
            className={`flex w-full items-center gap-3 rounded-2xl px-4 py-3 transition ${
              index === 0
                ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg"
                : "text-slate-300 hover:bg-white/5 hover:text-white"
            }`}
          >
            <Icon size={20} />
            {label}
          </button>
        ))}
      </nav>

      <div className="mt-10 rounded-2xl bg-gradient-to-br from-indigo-600/20 to-purple-600/20 border border-indigo-500/20 p-5">
        <h3 className="font-semibold text-white">
          AI Assistant
        </h3>

        <p className="mt-2 text-sm text-slate-400">
          Ask anything about your cloud infrastructure.
        </p>

        <button className="mt-5 w-full rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 py-3 font-medium text-white transition hover:opacity-90">
          Start Chat
        </button>
      </div>
    </aside>
  );
}