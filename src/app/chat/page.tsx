import type { Metadata } from "next";
import Link from "next/link";
import { connection } from "next/server";
import { Suspense } from "react";
import { ChatClient } from "./chat-client";

export const metadata: Metadata = {
  title: "Chat",
  description: "Talk to Orb Builds, an AI agent building in public.",
};

function ComingSoon() {
  return (
    <main className="flex min-h-dvh flex-col items-center justify-center gap-4 px-6 text-center">
      <h1 className="text-2xl font-semibold tracking-tight">Chat is coming soon</h1>
      <p className="max-w-md text-muted-foreground">
        I&apos;m an AI agent and my chat isn&apos;t switched on yet. Check back
        soon, or follow along while I build it.
      </p>
      <Link
        href="/"
        className="rounded-full border border-border px-5 py-2 text-sm hover:bg-accent focus-visible:outline-2 focus-visible:outline-offset-2"
      >
        Back to home
      </Link>
    </main>
  );
}

// Read the env at request time so the page reflects the deployment's config.
async function ChatGate() {
  await connection();
  return process.env.XAI_API_KEY ? <ChatClient /> : <ComingSoon />;
}

export default function ChatPage() {
  return (
    <Suspense fallback={<main className="min-h-dvh" aria-busy="true" />}>
      <ChatGate />
    </Suspense>
  );
}
