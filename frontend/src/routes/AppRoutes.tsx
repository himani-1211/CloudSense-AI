import { Navigate, Route, Routes } from "react-router-dom";

import Dashboard from "../pages/Dashboard/Dashboard";
import Login from "../pages/Login/Login";
import Settings from "../pages/Settings/Settings";
import DesignSystem from "../pages/DesignSystem/DesignSystem";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      <Route path="/login" element={<Login />} />

      <Route path="/dashboard" element={<Dashboard />} />

      <Route path="/settings" element={<Settings />} />

      <Route path="/design-system" element={<DesignSystem />} />
    </Routes>
  );
}