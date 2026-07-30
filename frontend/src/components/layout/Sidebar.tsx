import {
  LayoutDashboard,
  BrainCircuit,
  AlertTriangle,
  Cloud,
  Bot,
  Plug,
  FileText,
  Settings,
  ChevronDown,
} from "lucide-react";

import type { LucideIcon } from "lucide-react";

import { useNavigate, useLocation } from "react-router-dom";

interface MenuItem {
  icon: LucideIcon;
  label: string;
  path: string;
}

interface MenuSection {
  title: string;
  items: MenuItem[];
}

const sections: MenuSection[] = [
  {
    title: "OVERVIEW",
    items: [
      {
        icon: LayoutDashboard,
        label: "Dashboard",
        path: "/dashboard",
      },
    ],
  },
  {
    title: "INTELLIGENCE",
    items: [
      {
        icon: BrainCircuit,
        label: "Operations",
        path: "/operations",
      },
      {
        icon: AlertTriangle,
        label: "Incidents",
        path: "/incidents",
      },
      {
        icon: Bot,
        label: "AI Copilot",
        path: "/copilot",
      },
    ],
  },
  {
    title: "INFRASTRUCTURE",
    items: [
      {
        icon: Cloud,
        label: "Infrastructure",
        path: "/infrastructure",
      },
      {
        icon: Plug,
        label: "Integrations",
        path: "/integrations",
      },
    ],
  },
  {
    title: "WORKSPACE",
    items: [
      {
        icon: FileText,
        label: "Reports",
        path: "/reports",
      },
      {
        icon: Settings,
        label: "Settings",
        path: "/settings",
      },
    ],
  },
];

export default function Sidebar() {
  const navigate = useNavigate();

  const location = useLocation();

  return (
    <aside className="sticky top-6 flex h-[calc(100vh-48px)] w-[290px] flex-col rounded-3xl border border-white/10 bg-[#111827] px-6 py-6">
      {/* Logo */}
      <div className="-ml-7 flex items-center gap-1">
        <img
          src="/logo-icon.png"
          alt="CloudSense AI"
          className="h-22 w-22 object-contain"
        />

        <div>
          <h1
            className="text-2xl font-bold leading-none"
            style={{ fontFamily: "var(--font-heading)" }}
          >
            <span className="text-white">CloudSense </span>

            <span className="bg-gradient-to-r from-cyan-400 via-blue-500 to-violet-500 bg-clip-text text-transparent">
              AI
            </span>
          </h1>

          <p className="mt-2 text-[10px] uppercase tracking-[0.25em] text-slate-500">
            Multi-Cloud Intelligence
          </p>
        </div>
      </div>

      {/* Navigation */}
      <div className="mt-10 flex-1 overflow-y-auto">
        {sections.map((section) => (
          <div key={section.title} className="mb-8">
            <p className="mb-3 px-2 text-[10px] font-semibold tracking-[0.22em] text-slate-500">
              {section.title}
            </p>

            <div className="space-y-1.5">
              {section.items.map((item) => {
                const Icon = item.icon;

                const active = location.pathname === item.path;

                return (
                  <button
                    key={item.label}
                    onClick={() => navigate(item.path)}
                    className={`flex w-full items-center gap-3 rounded-xl px-3 py-3 text-sm transition-all duration-200 ${
                      active
                        ? "border border-cyan-500/20 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 text-white"
                        : "text-slate-400 hover:bg-white/5 hover:text-white"
                    }`}
                  >
                    <Icon size={18} />

                    <span className="truncate">
                      {item.label}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      {/* Workspace */}
      <div className="border-t border-white/10 pt-5">
        <button className="flex w-full items-center justify-between rounded-xl px-2 py-2 transition hover:bg-white/5">
          <div>
            <p className="text-sm font-medium text-white">
              Himani
            </p>

            <p className="text-xs text-slate-400">
              Default Workspace
            </p>
          </div>

          <ChevronDown
            size={16}
            className="text-slate-400"
          />
        </button>
      </div>
    </aside>
  );
}