import DashboardLayout from "../../layouts/DashboardLayout";
import Hero from "../../components/dashboard/Hero";
import KPISection from "../../components/dashboard/KPISection";

export default function Dashboard() {
  return (
    <DashboardLayout>
      <Hero />

      <KPISection />
    </DashboardLayout>
  );
}