import type {
  CourseOutline,
  ProgressOut,
  Quiz,
  QuizSubmitResult,
  SessionCreatedOut,
  SessionProgressOut,
} from "./types";
import { ApiError } from "./errors";

const API_BASE = import.meta.env.VITE_API_BASE ?? "";
const SESSION_TOKEN_KEY = "umpire-course-access-token";
const SESSION_FLAG_KEY = "umpire-course-has-session";
const LEGACY_SESSION_ID_KEY = "umpire-course-session-id";

/**
 * Bearer in localStorage is a last-resort Vite/dev fallback.
 * Prefer the httpOnly cookie (credentials: include). Only persist a bearer
 * when the API returns one (development / COURSE_EXPOSE_ACCESS_TOKEN=true).
 */
export function getStoredAccessToken(): string | null {
  return localStorage.getItem(SESSION_TOKEN_KEY);
}

export function hasStoredSessionFlag(): boolean {
  return localStorage.getItem(SESSION_FLAG_KEY) === "1" || Boolean(getStoredAccessToken());
}

export function markSessionPresent(): void {
  localStorage.setItem(SESSION_FLAG_KEY, "1");
  localStorage.removeItem(LEGACY_SESSION_ID_KEY);
}

export function storeAccessToken(token: string | null | undefined): void {
  markSessionPresent();
  if (token) {
    localStorage.setItem(SESSION_TOKEN_KEY, token);
  } else {
    localStorage.removeItem(SESSION_TOKEN_KEY);
  }
  localStorage.removeItem(LEGACY_SESSION_ID_KEY);
}

export function clearAccessToken(): void {
  localStorage.removeItem(SESSION_TOKEN_KEY);
  localStorage.removeItem(SESSION_FLAG_KEY);
  localStorage.removeItem(LEGACY_SESSION_ID_KEY);
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(init?.headers as Record<string, string> | undefined),
  };
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers,
    credentials: "include",
  });
  if (!res.ok) {
    await res.text().catch(() => "");
    throw new ApiError(res.status);
  }
  if (res.status === 204) {
    return undefined as T;
  }
  return res.json() as Promise<T>;
}

function authHeaders(token: string | null | undefined): Record<string, string> {
  // Only send Authorization when we actually have a bearer; otherwise rely on cookie.
  return token ? { Authorization: `Bearer ${token}` } : {};
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
  getProgress: (token?: string | null) =>
    request<SessionProgressOut>("/api/progress/session", {
      headers: authHeaders(token),
    }),
  updateProgress: (
    body: {
      module_id: string;
      status: "not_started" | "in_progress";
    },
    token?: string | null,
  ) =>
    request<ProgressOut>("/api/progress/session", {
      method: "PUT",
      headers: authHeaders(token),
      body: JSON.stringify(body),
    }),
  revokeSession: (token?: string | null) =>
    request<void>("/api/progress/session", {
      method: "DELETE",
      headers: authHeaders(token),
    }),
  submitQuiz: (
    quizId: string,
    answers: Array<{
      question_id: string;
      selected_option_id?: string;
      written_answer?: string;
    }>,
    options?: { saveProgress?: boolean; accessToken?: string | null },
  ) =>
    request<QuizSubmitResult>(`/api/quizzes/${quizId}/submit`, {
      method: "POST",
      headers: authHeaders(options?.accessToken),
      body: JSON.stringify({
        save_progress: Boolean(options?.saveProgress),
        answers,
      }),
    }),
};
