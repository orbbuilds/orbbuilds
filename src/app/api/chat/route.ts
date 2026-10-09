import { xai } from "@ai-sdk/xai";
import { frontendTools } from "@assistant-ui/ai-sdk";
import {
  convertToModelMessages,
  createUIMessageStreamResponse,
  streamText,
  toUIMessageStream,
} from "ai";
import type { UIMessage } from "ai";

export const maxDuration = 30;

// Requires XAI_API_KEY in the environment (see .env.example).
export async function POST(req: Request) {
  if (!process.env.XAI_API_KEY) {
    return Response.json({ error: "Chat is coming soon." }, { status: 503 });
  }
  const {
    messages,
    system,
    tools,
  }: { messages: UIMessage[]; system?: string; tools?: Parameters<typeof frontendTools>[0] } =
    await req.json();

  const aiSDKTools = { ...frontendTools(tools ?? {}) };

  const result = streamText({
    abortSignal: req.signal,
    model: xai(process.env.XAI_MODEL ?? "grok-4"),
    system:
      system ??
      "You are Orb Builds, an AI building AI products in public. Be direct, honest, and useful.",
    messages: await convertToModelMessages(messages, { tools: aiSDKTools }),
    tools: aiSDKTools,
  });

  return createUIMessageStreamResponse({
    stream: toUIMessageStream({ stream: result.stream }),
  });
}
