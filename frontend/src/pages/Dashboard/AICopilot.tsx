import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import {
  Bot,
  Send,
  Sparkles,
  BrainCircuit,
  WandSparkles,
  Clock3,
} from "lucide-react";

import {
  getCopilotSummary,
  chatWithCopilot,
  type CopilotSummary,
  type ChatMessage,
} from "../../api/copilot";

export default function AICopilot() {
  const [summary, setSummary] = useState<CopilotSummary | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(true);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    loadSummary();
  }, []);

  async function loadSummary() {
    try {
      setLoading(true);

      const data = await getCopilotSummary();

      setSummary(data);
      setMessages(data.conversation);
    } catch (err) {
      console.error(err);
      setError("Failed to load AI Copilot.");
    } finally {
      setLoading(false);
    }
  }

  async function sendMessage(message: string) {
    if (!message.trim()) return;

    const userMessage: ChatMessage = {
      role: "user",
      text: message,
      timestamp: "Just now",
    };

    setMessages((prev) => [...prev, userMessage]);

    setQuestion("");
    setSending(true);

    try {
      const response = await chatWithCopilot(message);

      const aiMessage: ChatMessage = {
        role: "assistant",
        text: response.answer,
        timestamp: "Just now",
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Unable to contact CloudSense AI.",
          timestamp: "Just now",
        },
      ]);
    } finally {
      setSending(false);
    }
  }

  if (loading) {
    return (
      <DashboardLayout>
        <div className="py-20 text-center text-slate-400">
          Loading AI Copilot...
        </div>
      </DashboardLayout>
    );
  }

  if (error) {
    return (
      <DashboardLayout>
        <div className="py-20 text-center text-red-400">
          {error}
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        {/* Header */}
        <div>
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-cyan-500/10 p-3 text-cyan-400">
              <Bot size={28} />
            </div>

            <div>
              <h1
                className="text-4xl font-bold text-white"
                style={{ fontFamily: "var(--font-heading)" }}
              >
                AI Copilot
              </h1>

              <p className="mt-2 text-slate-400">
                Ask questions, investigate incidents,
                understand infrastructure behaviour and
                receive AI-powered recommendations.
              </p>
            </div>
          </div>
        </div>

        {/* Suggested Questions */}
        <div>
          <h2 className="mb-4 text-lg font-semibold text-white">
            Suggested Questions
          </h2>

          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            {summary?.suggested_questions.map((item) => (
              <PromptCard
                key={item.text}
                text={item.text}
                onClick={() => sendMessage(item.text)}
              />
            ))}
          </div>
        </div>

        {/* Chat */}
        <div className="rounded-3xl border border-white/10 bg-[#151C31]">
          <div className="space-y-6 p-8">
            {messages.map((message, index) =>
              message.role === "assistant" ? (
                <AIMessage
                  key={index}
                  text={message.text}
                  timestamp={message.timestamp}
                />
              ) : (
                <Message
                  key={index}
                  user
                  text={message.text}
                />
              )
            )}
          </div>

          <div className="border-t border-white/10 p-6">
            <div className="flex items-center gap-4 rounded-2xl border border-white/10 bg-[#101728] px-5 py-4">
              <input
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    sendMessage(question);
                  }
                }}
                placeholder="Ask CloudSense AI anything..."
                className="flex-1 bg-transparent text-white outline-none placeholder:text-slate-500"
              />

              <button
                disabled={sending}
                onClick={() => sendMessage(question)}
                className="rounded-xl bg-cyan-500 p-3 text-white transition hover:bg-cyan-400 disabled:opacity-50"
              >
                <Send size={18} />
              </button>
            </div>
          </div>
        </div>

        {/* Capabilities */}
        <div className="grid gap-6 md:grid-cols-3">
          {summary?.capabilities.map((capability) => (
            <CapabilityCard
              key={capability.title}
              icon={
                capability.title.includes("Infrastructure") ? (
                  <BrainCircuit size={22} />
                ) : capability.title.includes("Security") ? (
                  <Sparkles size={22} />
                ) : (
                  <WandSparkles size={22} />
                )
              }
              title={capability.title}
              description={capability.description}
            />
          ))}
        </div>
      </div>
    </DashboardLayout>
  );
}
function PromptCard({
  text,
  onClick,
}: {
  text: string;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      className="rounded-2xl border border-white/10 bg-[#151C31] p-5 text-left transition hover:border-cyan-500/20 hover:bg-[#18233D]"
    >
      <p className="text-white">{text}</p>
    </button>
  );
}

function Message({
  user,
  text,
}: {
  user?: boolean;
  text: string;
}) {
  return (
    <div className={`flex ${user ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-2xl whitespace-pre-wrap rounded-2xl px-5 py-4 ${
          user
            ? "bg-cyan-500 text-white"
            : "bg-[#101728] text-slate-300"
        }`}
      >
        {text}
      </div>
    </div>
  );
}

function AIMessage({
  text,
  timestamp,
}: {
  text: string;
  timestamp: string;
}) {
  return (
    <div className="flex justify-start">
      <div className="max-w-4xl rounded-2xl bg-[#101728] p-6">
        <div className="mb-4 flex items-center gap-3">
          <div className="rounded-xl bg-cyan-500/10 p-2 text-cyan-400">
            <Bot size={18} />
          </div>

          <div>
            <h3 className="font-semibold text-white">
              CloudSense AI
            </h3>

            <div className="mt-1 flex items-center gap-2 text-xs text-slate-500">
              <Clock3 size={13} />
              {timestamp}
            </div>
          </div>
        </div>

        <div className="whitespace-pre-wrap leading-7 text-slate-300">
          {text}
        </div>
      </div>
    </div>
  );
}

function CapabilityCard({
  icon,
  title,
  description,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
}) {
  return (
    <div className="rounded-3xl border border-white/10 bg-[#151C31] p-6">
      <div className="mb-5 inline-flex rounded-2xl bg-cyan-500/10 p-4 text-cyan-400">
        {icon}
      </div>

      <h3 className="text-xl font-semibold text-white">
        {title}
      </h3>

      <p className="mt-3 leading-7 text-slate-400">
        {description}
      </p>
    </div>
  );
}