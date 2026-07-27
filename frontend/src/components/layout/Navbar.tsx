import { Bell, Search } from "lucide-react";

export default function Navbar() {
  return (
    <header className="flex h-20 items-center justify-between rounded-3xl border border-white/10 bg-[#111827] px-6">

      <div className="flex h-12 w-[420px] items-center gap-3 rounded-2xl bg-[#1A2238] px-4">

        <Search size={18} className="text-slate-400" />

        <input
          placeholder="Search anything..."
          className="w-full bg-transparent text-white outline-none placeholder:text-slate-500"
        />

      </div>

      <div className="flex items-center gap-4">

        <button className="rounded-xl bg-[#1A2238] p-3 text-slate-300 hover:text-white">
          <Bell size={20} />
        </button>

        <button className="rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 px-5 py-3 font-medium text-white">
          AI Assistant
        </button>

        <div className="h-11 w-11 rounded-full bg-slate-600" />

      </div>

    </header>
  );
}