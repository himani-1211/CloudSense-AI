import DashboardLayout from "../../layouts/DashboardLayout";
import {
  User,
  Bell,
  Shield,
  KeyRound,
  Cloud,
  ChevronRight,
} from "lucide-react";

export default function Settings() {
  const sections = [
    {
      icon: <User size={20} />,
      title: "Profile",
      desc: "Manage your account information and preferences.",
    },
    {
      icon: <Bell size={20} />,
      title: "Notifications",
      desc: "Configure alerts and notification channels.",
    },
    {
      icon: <Shield size={20} />,
      title: "Security",
      desc: "Passwords, MFA and access management.",
    },
    {
      icon: <KeyRound size={20} />,
      title: "API Keys",
      desc: "Generate and manage API credentials.",
    },
    {
      icon: <Cloud size={20} />,
      title: "Cloud Integrations",
      desc: "Manage connected cloud accounts and permissions.",
    },
  ];

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div>
          <h1
            className="text-4xl font-bold text-white"
            style={{ fontFamily: "var(--font-heading)" }}
          >
            Settings
          </h1>

          <p className="mt-2 text-slate-400">
            Configure your CloudSense AI workspace and account preferences.
          </p>
        </div>

        <div className="rounded-3xl border border-white/10 bg-[#151C31] overflow-hidden">
          {sections.map((item, index) => (
            <div
              key={item.title}
              className={`flex items-center justify-between p-6 transition hover:bg-white/5 ${
                index !== sections.length - 1
                  ? "border-b border-white/10"
                  : ""
              }`}
            >
              <div className="flex items-center gap-5">
                <div className="rounded-xl bg-cyan-500/10 p-3 text-cyan-400">
                  {item.icon}
                </div>

                <div>
                  <h3 className="text-lg font-semibold text-white">
                    {item.title}
                  </h3>

                  <p className="mt-1 text-sm text-slate-400">
                    {item.desc}
                  </p>
                </div>
              </div>

              <ChevronRight className="text-slate-500" size={20} />
            </div>
          ))}
        </div>

        <div className="rounded-3xl border border-cyan-500/20 bg-gradient-to-r from-cyan-500/10 via-blue-500/10 to-violet-500/10 p-6">
          <h2 className="text-xl font-semibold text-white">
            Workspace Status
          </h2>

          <div className="mt-6 grid gap-5 md:grid-cols-3">
            <StatusCard title="Workspace" value="Healthy" />
            <StatusCard title="AI Services" value="Online" />
            <StatusCard title="Connected Clouds" value="3 Active" />
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

function StatusCard({
  title,
  value,
}: {
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-2xl bg-[#151C31] p-6 border border-white/10">
      <p className="text-xs uppercase tracking-[0.18em] text-slate-500">
        {title}
      </p>

      <h3 className="mt-2 text-2xl font-bold text-white">
        {value}
      </h3>
    </div>
  );
}