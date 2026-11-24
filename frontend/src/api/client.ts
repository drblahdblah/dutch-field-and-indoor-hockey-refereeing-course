import type {
  CourseOutline,
  Quiz,
  QuizSubmitResult,
  SessionCreatedOut,
  SessionProgressOut,
} from "./types";

const API_BASE = import.meta.env.VITE_API_BASE ?? "";
const SESSION_TOKEN_KEY = "umpire-course-access-token";

export function getStoredAccessToken(): string | null {
  return localStorage.getItem(SESSION_TOKEN_KEY);
}

export function storeAccessToken(token: string): void {
  localStorage.setItem(SESSION_TOKEN_KEY, token);
}

export function clearAccessToken(): void {
  localStorage.removeItem(SESSION_TOKEN_KEY);
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(init?.headers as Record<string, string> | undefined),
  };
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers,
  });
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`${res.status}: ${detail || res.statusText}`);
  }
  return res.json() as Promise<T>;
}

function authHeaders(token: string): Record<string, string> {
  return { Authorization: `Bearer ${token}` };
}

export const api = {
  health: () => request<{ status: string }>("/api/health"),
  course: () => request<CourseOutline>("/api/course"),
  quiz: (id: string) => request<Quiz>(`/api/course/quizzes/${id}`),
  createSession: (displayName?: string, locale = "nl") =>
    request<SessionCreatedOut>("/api/progress/sessions", {
      method: "POST",
      body: JSON.stringify({ display_name: displayName ?? null, locale }),
    }),
  getProgress: (token: string) =>
    request<SessionProgressOut>("/api/progress/session", {
      headers: authHeaders(token),
    }),
  updateProgress: (
    token: string,
    body: {
      module_id: string;
      status: "not_started" | "in_progress" | "completed";
      last_question_id?: string;
    },
  ) =>
    request("/api/progress/session", {
      method: "PUT",
      headers: authHeaders(token),
      body: JSON.stringify(body),
    }),
  submitQuiz: (
    quizId: string,
    answers: Array<{
      question_id: string;
      selected_option_id?: string;
      written_answer?: string;
    }>,
    accessToken?: string | null,
  ) =>
    request<QuizSubmitResult>(`/api/quizzes/${quizId}/submit`, {
      method: "POST",
      headers: accessToken ? authHeaders(accessToken) : undefined,
      body: JSON.stringify({
        save_progress: Boolean(accessToken),
        answers,
      }),
    }),
};
