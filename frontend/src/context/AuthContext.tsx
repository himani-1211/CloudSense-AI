import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";

import {
  login as loginApi,
  getCurrentUser,
} from "../api/auth";

import {
  getToken,
  setToken,
  removeToken,
} from "../utils/token";

import type {
  LoginData,
  User,
} from "../types/auth";

interface AuthContextType {
  user: User | null;
  loading: boolean;
  isAuthenticated: boolean;
  login: (data: LoginData) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export function AuthProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    initializeAuth();
  }, []);

  async function initializeAuth() {
    const token = getToken();

    if (!token) {
      setLoading(false);
      return;
    }

    try {
      const currentUser = await getCurrentUser();
      setUser(currentUser);
    } catch {
      removeToken();
      setUser(null);
    } finally {
      setLoading(false);
    }
  }

  async function login(data: LoginData) {
    const response = await loginApi(data);

    setToken(response.access_token);

    const currentUser = await getCurrentUser();

    setUser(currentUser);
  }

  function logout() {
    removeToken();
    setUser(null);
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated: !!user,
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used inside AuthProvider"
    );
  }

  return context;
}