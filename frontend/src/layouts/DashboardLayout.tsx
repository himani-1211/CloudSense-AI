import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

interface DashboardLayoutProps {
  children: React.ReactNode;
}

export default function DashboardLayout({
  children,
}: DashboardLayoutProps) {
  return (
    <div className="min-h-screen bg-[#0B1020]">
      <div className="flex p-5 gap-5">

        {/* Sidebar */}

        <Sidebar />

        {/* Main */}

        <div className="flex-1">

          <Navbar />

          <main className="mt-5">
            {children}
          </main>

        </div>

      </div>
    </div>
  );
}