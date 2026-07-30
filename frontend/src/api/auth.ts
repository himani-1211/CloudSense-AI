import api from "./axios";
import type {
  LoginData,
  RegisterData,
  TokenResponse,
  User,
} from "../types/auth";

export const register = async (data: RegisterData) => {
  const response = await api.post("/auth/register", data);
  return response.data;
};

export const login = async (data: LoginData): Promise<TokenResponse> => {
  const formData = new URLSearchParams();

  formData.append("username", data.email);
  formData.append("password", data.password);

  const response = await api.post(
    "/auth/login",
    formData,
    {
      headers: {
        "Content-Type":
          "application/x-www-form-urlencoded",
      },
    }
  );

  return response.data;
};

export const getCurrentUser = async (): Promise<User> => {
  const response = await api.get("/auth/me");
  return response.data;
};