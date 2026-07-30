import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import {
  Cloud,
  CheckCircle2,
  Plus,
  Search,
  Filter,
  ArrowRight,
  ShieldCheck,
  RefreshCw,
} from "lucide-react";

import { getIntegrationsSummary } from "../../api/integration";
import type {
  IntegrationsSummary,
  IntegrationItem,
} from "../../api/integration";

export default function Integrations() {
  const [data, setData] = useState<IntegrationsSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchIntegrations = async () => {
      try {
        setLoading(true);
        const response = await getIntegrationsSummary();
        setData(response);
      } catch (err) {
        console.error(err);
        setError("Failed to load integrations.");
      } finally {
        setLoading(false);
      }
    };

    fetchIntegrations();
  }, []);

  const filteredIntegrations = useMemo(() => {
    if (!data) return [];

    return data.integrations.filter(
      (integration) =>
        integration.name.toLowerCase().includes(search.toLowerCase()) ||
        integration.category.toLowerCase().includes(search.toLowerCase()) ||
        integration.status.toLowerCase().includes(search.toLowerCase())
    );
  }, [data, search]);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex h-96 items-center justify-center">
          <p className="text-slate-400">Loading integrations...</p>
        </div>
      </DashboardLayout>
    );
  }

  if (error || !data) {
    return (
      <DashboardLayout>
        <div className="flex h-96 items-center justify-center">
          <p className="text-red-400">
            {error || "Unable to load integrations."}
          </p>
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
              Integrations
            </h1>

            <p className="mt-2 text-slate-400">
              Connect cloud providers, monitoring platforms and DevOps tools to
              enable unified AI-powered operations.
            </p>
          </div>

          <button className="flex items-center gap-2 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 px-5 py-3 font-medium text-white transition hover:opacity-90">
            <Plus size={18} />
            Add Integration
          </button>
        </div>

        {/* Search */}
        <div className="flex h-12 items-center gap-3 rounded-2xl border border-white/10 bg-[#151C31] px-4">
          <Search size={18} className="text-slate-400" />

          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search integrations..."
            className="w-full bg-transparent text-white outline-none placeholder:text-slate-500"
          />

          <Filter className="text-slate-400" size={18} />
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4">
          <SummaryCard
            title="Connected"
            value={String(data.summary.connected)}
          />

          <SummaryCard
            title="Available"
            value={String(data.summary.available)}
          />

          <SummaryCard
            title="Healthy"
            value={String(data.summary.healthy)}
          />

          <SummaryCard
            title="Sync Rate"
            value={data.summary.sync_rate}
          />
        </div>

        {/* Integration Grid */}
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">
          {filteredIntegrations.length === 0 ? (
            <div className="col-span-full rounded-2xl border border-white/10 bg-[#151C31] p-8 text-center text-slate-400">
              No integrations found.
            </div>
          ) : (
            filteredIntegrations.map((integration: IntegrationItem) => (
              <IntegrationCard
                key={integration.name}
                name={integration.name}
                category={integration.category}
                status={integration.status}
              />
            ))
          )}
        </div>

        {/* AI Recommendation */}
        <div className="rounded-3xl border border-cyan-500/20 bg-gradient-to-r from-cyan-500/10 via-blue-500/10 to-violet-500/10 p-6">
          <div className="flex items-start gap-5">
            <div className="rounded-2xl bg-cyan-500/15 p-4 text-cyan-400">
              <ShieldCheck size={28} />
            </div>

            <div className="flex-1">
              <h2 className="text-xl font-semibold text-white">
                {data.ai_recommendation.title}
              </h2>

              <p className="mt-3 leading-7 text-slate-300">
                {data.ai_recommendation.description}
              </p>

              <button className="mt-5 flex items-center gap-2 rounded-xl bg-cyan-500 px-5 py-3 text-white transition hover:bg-cyan-400">
                Learn More
                <ArrowRight size={18} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}
function SummaryCard({
  title,
  value,
}: {
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6">
      <div className="mb-5 inline-flex rounded-xl bg-cyan-500/10 p-3 text-cyan-400">
        <RefreshCw size={20} />
      </div>

      <p className="text-xs uppercase tracking-[0.18em] text-slate-500">
        {title}
      </p>

      <h3 className="mt-2 text-3xl font-bold text-white">
        {value}
      </h3>
    </div>
  );
}

interface IntegrationCardProps {
  name: string;
  category: string;
  status: string;
}

function IntegrationCard({
  name,
  category,
  status,
}: IntegrationCardProps) {
  const connected = status === "Connected";
  const comingSoon = status === "Coming Soon";

  return (
    <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6 transition hover:border-cyan-500/20">
      <div className="flex items-center justify-between">
        <div className="rounded-2xl bg-cyan-500/10 p-4 text-cyan-400">
          <Cloud size={24} />
        </div>

        {connected ? (
          <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-xs text-emerald-400">
            Connected
          </span>
        ) : comingSoon ? (
          <span className="rounded-full bg-blue-500/10 px-3 py-1 text-xs text-blue-400">
            Coming Soon
          </span>
        ) : (
          <span className="rounded-full bg-yellow-500/10 px-3 py-1 text-xs text-yellow-400">
            Not Connected
          </span>
        )}
      </div>

      <h3 className="mt-6 text-xl font-semibold text-white">
        {name}
      </h3>

      <p className="mt-2 text-sm text-slate-400">
        {category}
      </p>

      <div className="mt-6 flex items-center justify-between">
        <div className="flex items-center gap-2 text-cyan-400">
          <CheckCircle2 size={16} />
          <span className="text-sm">{status}</span>
        </div>

        <ArrowRight size={18} className="text-slate-500" />
      </div>
    </div>
  );
}