import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

interface DashboardLayoutProps {
  children: React.ReactNode;
}

export default function DashboardLayout({
  children,
}: DashboardLayoutProps) {
  return (
    <div className="min-h-screen bg-[#0B1020] text-white">
      <div className="flex min-h-screen p-6 gap-6">
        {/* Sidebar */}
        <Sidebar />

        {/* Main Content */}
        <div className="flex-1 flex flex-col min-w-0">
          <Navbar />

          <main className="flex-1 mt-8 pb-8">
            <div className="mx-auto w-full max-w-[1440px]">
              {children}
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}