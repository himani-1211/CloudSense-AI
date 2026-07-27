import {
  BrainCircuit,
  DollarSign,
  Server,
  ShieldCheck,
} from "lucide-react";

import KPICard from "./KPICard";

export default function KPISection() {
  return (
    <section className="mb-8 grid grid-cols-4 gap-6">

      <KPICard
        title="Total Cloud Spend"
        value="$12,480"
        trend="+8.2%"
        icon={<DollarSign size={28} />}
        iconBg="rgba(99,102,241,0.18)"
        iconColor="#818CF8"
      />

      <KPICard
        title="Active Resources"
        value="426"
        trend="+12.4%"
        icon={<Server size={28} />}
        iconBg="rgba(59,130,246,0.18)"
        iconColor="#60A5FA"
      />

      <KPICard
        title="Security Score"
        value="92 / 100"
        trend="+5 pts"
        icon={<ShieldCheck size={28} />}
        iconBg="rgba(16,185,129,0.18)"
        iconColor="#34D399"
      />

      <KPICard
        title="AI Savings"
        value="$184"
        trend="+18.7%"
        icon={<BrainCircuit size={28} />}
        iconBg="rgba(249,115,22,0.18)"
        iconColor="#FB923C"
      />

    </section>
  );
}