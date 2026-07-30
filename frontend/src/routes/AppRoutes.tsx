import { Navigate, Route, Routes } from "react-router-dom";

import Dashboard from "../pages/Dashboard/Dashboard";
import Login from "../pages/Login/Login";
import Settings from "../pages/Settings/Settings";
import DesignSystem from "../pages/DesignSystem/DesignSystem";
import AWSConnect from "../pages/AWSConnect/AWSConnect";
import Infrastructure from "../pages/Dashboard/Infrastructure";
import Operations from "../pages/Dashboard/Operations"; 
import Incidents from "../pages/Dashboard/Incidents";
import Integrations from "../pages/Dashboard/Integrations";
import AICopilot from "../pages/Dashboard/AICopilot";

import ProtectedRoute from "./ProtectedRoute";
import Reports from "../pages/Dashboard/Reports";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace />} />

      <Route path="/login" element={<Login />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/settings"
        element={
          <ProtectedRoute>
            <Settings />
          </ProtectedRoute>
        }
      />

      <Route
        path="/connect-aws"
        element={
          <ProtectedRoute>
            <AWSConnect />
          </ProtectedRoute>
        }
      />

      <Route
        path="/infrastructure"
        element={
          <ProtectedRoute>
            <Infrastructure />
          </ProtectedRoute>
        }
      />

      <Route
        path="/operations"
        element={
          <ProtectedRoute>
            <Operations />
          </ProtectedRoute>
        }
      />

      <Route
        path="/incidents"
        element={
          <ProtectedRoute>
            <Incidents />
          </ProtectedRoute>
        }
      />

      <Route
        path="/reports"
        element={
          <ProtectedRoute>
            <Reports />
          </ProtectedRoute>
        }
      />

      <Route
        path="/integrations"
        element={
          <ProtectedRoute>
            <Integrations />
          </ProtectedRoute>
        }
      />

      <Route
        path="/copilot"
        element={
          <ProtectedRoute>
            <AICopilot />
          </ProtectedRoute>
        }
      />

      <Route
        path="/design-system"
        element={
          <ProtectedRoute>
            <DesignSystem />
          </ProtectedRoute>
        }
      />

      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}