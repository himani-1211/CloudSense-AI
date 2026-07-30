import api from "./axios";

export interface AWSConnectRequest {
  access_key: string;
  secret_key: string;
  region: string;
}

export interface AWSConnectResponse {
  message: string;
}

export async function connectAWS(data: AWSConnectRequest) {
  const response = await api.post<AWSConnectResponse>(
    "/aws/connect",
    data
  );

  return response.data;
}

// ---------- AWS Status ----------

export interface AWSStatusResponse {
  connected: boolean;
}

export async function getAWSStatus() {
  const response = await api.get<AWSStatusResponse>("/aws/status");
  return response.data;
}