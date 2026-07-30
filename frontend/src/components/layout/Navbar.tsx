import {
  Bell,
  ChevronDown,
  Search,
  Settings,
  User,
  LogOut,
} from "lucide-react";
import { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  const dropdownRef = useRef<HTMLDivElement>(null);

  const navigate = useNavigate();

  const { logout } = useAuth();

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () =>
      document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const handleLogout = () => {
    setOpen(false);
    logout();
    navigate("/login", { replace: true });
  };

  const handleSettings = () => {
    setOpen(false);
    navigate("/settings");
  };

  const handleProfile = () => {
    setOpen(false);
    // Navigate when profile page is available
    // navigate("/profile");
  };

  return (
    <header className="flex h-[72px] items-center justify-between rounded-3xl border border-white/10 bg-[#111827] px-7">
      {/* Search */}
      <div className="flex h-11 w-[360px] items-center gap-3 rounded-xl border border-white/10 bg-[#0F172A] px-4">
        <Search size={18} className="text-slate-400" />

        <input
          placeholder="Search incidents, resources, integrations..."
          className="w-full bg-transparent text-sm text-white outline-none placeholder:text-slate-500"
        />
      </div>

      {/* Right */}
      <div className="flex items-center gap-3">
        {/* Notifications */}
        <button className="relative flex h-11 w-11 items-center justify-center rounded-xl border border-white/10 bg-[#0F172A] text-slate-300 transition hover:border-cyan-500/30 hover:text-white">
          <Bell size={18} />

          <span className="absolute right-3 top-3 h-2 w-2 rounded-full bg-cyan-400" />
        </button>

        {/* Profile */}
        <div ref={dropdownRef} className="relative">
          <button
            onClick={() => setOpen((prev) => !prev)}
            className="flex items-center gap-3 rounded-xl border border-white/10 bg-[#0F172A] px-3 py-2 transition hover:border-cyan-500/30"
          >
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-r from-cyan-500 to-blue-600 font-semibold text-white">
              H
            </div>

            <div className="hidden text-left md:block">
              <p className="text-sm font-medium text-white">Himani</p>
              <p className="text-xs text-slate-400">Administrator</p>
            </div>

            <ChevronDown
              size={16}
              className={`text-slate-400 transition-transform ${
                open ? "rotate-180" : ""
              }`}
            />
          </button>

          {open && (
            <div className="absolute right-0 z-50 mt-3 w-56 overflow-hidden rounded-2xl border border-white/10 bg-[#161B22] shadow-2xl">
              <button
                onClick={handleProfile}
                className="flex w-full items-center gap-3 px-5 py-3 text-slate-300 transition hover:bg-white/5 hover:text-white"
              >
                <User size={17} />
                My Profile
              </button>

              <button
                onClick={handleSettings}
                className="flex w-full items-center gap-3 px-5 py-3 text-slate-300 transition hover:bg-white/5 hover:text-white"
              >
                <Settings size={17} />
                Settings
              </button>

              <div className="border-t border-white/10" />

              <button
                onClick={handleLogout}
                className="flex w-full items-center gap-3 px-5 py-3 text-red-400 transition hover:bg-red-500 hover:text-white"
              >
                <LogOut size={17} />
                Logout
              </button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}