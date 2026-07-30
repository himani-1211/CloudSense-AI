import { useEffect, useMemo, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import { Search, Cloud, Server, Database, HardDrive, Cpu, Activity } from "lucide-react";
import { getInfrastructureSummary } from "../../api/infrastructure";
import type { InfrastructureSummary, InfrastructureResource } from "../../api/infrastructure";

export default function Infrastructure() {
  const [data, setData] = useState<InfrastructureSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    (async () => {
      try {
        setData(await getInfrastructureSummary());
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const resources = useMemo(() => {
    if (!data) return [];
    return data.resources.filter(r =>
      (r.title + r.type + r.status).toLowerCase().includes(search.toLowerCase())
    );
  }, [data, search]);

  if (loading) return <DashboardLayout><div className="py-24 text-center text-slate-400">Loading infrastructure...</div></DashboardLayout>;
  if (!data) return <DashboardLayout><div className="py-24 text-center text-red-400">Failed to load infrastructure.</div></DashboardLayout>;

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div>
          <h1 className="text-4xl font-bold text-white">Infrastructure</h1>
          <p className="mt-2 text-slate-400">Live AWS infrastructure overview.</p>
        </div>

        <div className="flex h-12 items-center gap-3 rounded-2xl border border-white/10 bg-[#151C31] px-4">
          <Search size={18} className="text-slate-400" />
          <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search resources..." className="w-full bg-transparent text-white outline-none"/>
        </div>

        <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4">
          <Card icon={<Cloud size={20}/>} title="Cloud Providers" value={String(data.overview.cloud_providers)} />
          <Card icon={<Server size={20}/>} title="Compute Instances" value={String(data.overview.compute_instances)} />
          <Card icon={<Database size={20}/>} title="Databases" value={String(data.overview.databases)} />
          <Card icon={<HardDrive size={20}/>} title="Storage Buckets" value={String(data.overview.storage_buckets)} />
        </div>

        <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">
          <div className="xl:col-span-2 rounded-3xl border border-white/10 bg-[#151C31] p-6">
            <h2 className="mb-6 text-xl font-semibold text-white">AWS Resources</h2>
            <div className="space-y-3">{resources.map((r,i)=><Resource key={i} item={r} />)}</div>
          </div>

          <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6 space-y-5">
            <div className="rounded-2xl bg-cyan-500/10 p-5"><Activity className="text-cyan-400"/><p className="mt-2 text-xs text-slate-400">Overall Health</p><h2 className="text-4xl font-bold text-white">{data.health.overall_health}%</h2></div>
            <div className="rounded-2xl border border-white/10 p-5"><Cpu className="text-violet-400"/><p className="mt-2 text-xs text-slate-400">Average CPU Usage</p><h2 className="text-3xl font-bold text-white">{data.health.average_cpu_usage}%</h2></div>
            <div className="rounded-2xl border border-white/10 p-5"><p className="text-xs text-slate-400">AI Recommendation</p><p className="mt-2 text-white">{data.health.ai_recommendation}</p></div>
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

function Card({icon,title,value}:{icon:React.ReactNode,title:string;value:string}) {
 return <div className="rounded-2xl border border-white/10 bg-[#151C31] p-6"><div className="mb-4 text-cyan-400">{icon}</div><p className="text-xs text-slate-500">{title}</p><h3 className="mt-2 text-3xl font-bold text-white">{value}</h3></div>;
}

function Resource({item}:{item:InfrastructureResource}) {
 return <div className="rounded-2xl border border-white/10 p-5"><div className="flex justify-between"><div><h3 className="font-semibold text-white">{item.title}</h3><p className="text-sm text-slate-400">{item.type}</p></div><span className="text-cyan-400">{item.status}</span></div><div className="mt-4 grid grid-cols-2 gap-4"><div><p className="text-xs text-slate-500">Utilization</p><p className="text-white">{item.utilization}</p></div><div><p className="text-xs text-slate-500">Uptime</p><p className="text-white">{item.uptime}</p></div></div></div>;
}