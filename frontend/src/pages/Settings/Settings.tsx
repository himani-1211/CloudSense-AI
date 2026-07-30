import { useEffect, useState } from "react";
import {
  CheckCircle2,
  Cloud,
  BrainCircuit,
  Settings as SettingsIcon,
  ChevronRight,
} from "lucide-react";

import DashboardLayout from "../../layouts/DashboardLayout";
import {
  getSettingsSummary,
} from "../../api/settings";
import type {
  SettingsSummary,
  SettingItem,
} from "../../api/settings";

export default function Settings() {
  const [settings, setSettings] =
    useState<SettingsSummary | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadSettings() {
      try {
        const data = await getSettingsSummary();
        setSettings(data);
      } catch (err) {
        console.error("Failed to load settings:", err);
      } finally {
        setLoading(false);
      }
    }

    loadSettings();
  }, []);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="py-24 text-center text-slate-400">
          Loading settings...
        </div>
      </DashboardLayout>
    );
  }

  if (!settings) {
    return (
      <DashboardLayout>
        <div className="py-24 text-center text-red-400">
          Failed to load settings.
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <section className="space-y-8">
        {/* Header */}
        <div>
          <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-cyan-500/20 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
            <SettingsIcon size={16} />
            Workspace Configuration
          </div>

          <h1 className="text-5xl font-bold text-white">
            Settings
          </h1>

          <p className="mt-4 max-w-3xl text-lg text-slate-400">
            Manage your CloudSense workspace, cloud integrations,
            security and platform preferences.
          </p>
        </div>

        {/* Workspace Status */}
        <div className="grid grid-cols-1 gap-5 md:grid-cols-3">
          <StatusCard
            icon={<CheckCircle2 size={22} />}
            title="Workspace"
            value={settings.workspace_status.workspace}
          />

          <StatusCard
            icon={<BrainCircuit size={22} />}
            title="AI Services"
            value={settings.workspace_status.ai_services}
          />

          <StatusCard
            icon={<Cloud size={22} />}
            title="Connected Clouds"
            value={settings.workspace_status.connected_clouds}
          />
        </div>

        {/* Sections */}
        <div className="rounded-3xl border border-white/10 bg-[#151C31] p-8">
          <h2 className="text-2xl font-semibold text-white">
            Configuration Sections
          </h2>

          <p className="mt-2 text-slate-400">
            Configure different parts of your CloudSense workspace.
          </p>

          <div className="mt-8 space-y-4">
            {settings.sections.map((section, index) => (
              <SettingCard
                key={index}
                item={section}
              />
            ))}
          </div>
        </div>
      </section>
    </DashboardLayout>
  );
}

function StatusCard({
  icon,
  title,
  value,
}: {
  icon: React.ReactNode;
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6 transition hover:border-cyan-500/20">
      <div className="mb-5 inline-flex rounded-xl bg-cyan-500/10 p-3 text-cyan-400">
        {icon}
      </div>

      <p className="text-xs uppercase tracking-[0.15em] text-slate-500">
        {title}
      </p>

      <h3 className="mt-2 text-2xl font-bold text-white">
        {value}
      </h3>
    </div>
  );
}

function SettingCard({
  item,
}: {
  item: SettingItem;
}) {
  return (
    <div className="flex items-center justify-between rounded-2xl border border-white/10 p-6 transition hover:border-cyan-500/20 hover:bg-white/5">
      <div>
        <h3 className="text-lg font-semibold text-white">
          {item.title}
        </h3>

        <p className="mt-2 text-sm text-slate-400">
          {item.description}
        </p>
      </div>

      <ChevronRight
        size={20}
        className="text-slate-500"
      />
    </div>
  );
}