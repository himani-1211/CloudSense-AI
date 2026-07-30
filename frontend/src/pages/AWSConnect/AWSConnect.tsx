import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Eye, EyeOff } from "lucide-react";
import { connectAWS } from "../../api/aws";

export default function AWSConnect() {
  const navigate = useNavigate();

  const [accessKey, setAccessKey] = useState("");
  const [secretKey, setSecretKey] = useState("");
  const [region, setRegion] = useState("us-east-1");

  const [showSecret, setShowSecret] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    setLoading(true);
    setError("");

    try {
      await connectAWS({
        access_key: accessKey,
        secret_key: secretKey,
        region,
      });

      navigate("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to connect AWS account.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-950">
      <div className="w-full max-w-lg rounded-3xl border border-slate-800 bg-slate-900 p-8 shadow-2xl">
        <h1 className="mb-2 text-3xl font-bold text-white">
          Connect AWS
        </h1>

        <p className="mb-8 text-slate-400">
          Connect your AWS account to start monitoring your cloud resources.
        </p>

        <form onSubmit={handleSubmit} className="space-y-5">

          <input
            type="text"
            placeholder="AWS Access Key"
            className="w-full rounded-xl border border-slate-700 bg-slate-800 p-3 text-white"
            value={accessKey}
            onChange={(e) => setAccessKey(e.target.value)}
            required
          />

          <div className="relative">
            <input
              type={showSecret ? "text" : "password"}
              placeholder="AWS Secret Key"
              className="w-full rounded-xl border border-slate-700 bg-slate-800 p-3 pr-12 text-white"
              value={secretKey}
              onChange={(e) => setSecretKey(e.target.value)}
              required
            />

            <button
              type="button"
              onClick={() => setShowSecret(!showSecret)}
              className="absolute right-3 top-3 text-slate-400"
            >
              {showSecret ? <EyeOff size={20} /> : <Eye size={20} />}
            </button>
          </div>

          <select
            className="w-full rounded-xl border border-slate-700 bg-slate-800 p-3 text-white"
            value={region}
            onChange={(e) => setRegion(e.target.value)}
          >
            <option>us-east-1</option>
            <option>us-east-2</option>
            <option>us-west-1</option>
            <option>us-west-2</option>
            <option>ap-south-1</option>
            <option>eu-west-1</option>
          </select>

          {error && (
            <p className="text-red-500">{error}</p>
          )}

          <button
            disabled={loading}
            className="w-full rounded-xl bg-indigo-600 py-3 font-semibold text-white transition hover:bg-indigo-700 disabled:opacity-50"
          >
            {loading ? "Connecting..." : "Connect AWS"}
          </button>

        </form>
      </div>
    </div>
  );
}