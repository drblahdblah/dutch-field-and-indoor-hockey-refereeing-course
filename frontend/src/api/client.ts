import type {
  CourseOutline,
  Quiz,
  QuizSubmitResult,
  SessionOut,
  SessionProgressOut,
} from "./types";

const API_BASE = import.meta.env.VITE_API_BASE ?? "";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(init?.headers ?? {}) },
    ...init,
  });
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`${res.status}: ${detail || res.statusText}`);
  }
  return res.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>("/api/health"),
  course: () => request<CourseOutline>("/api/course"),
  quiz: (id: string) => request<Quiz>(`/api/course/quizzes/${id}`),
  createSession: (displayName?: string, locale = "nl") =>
    request<SessionOut>("/api/progress/sessions", {
      method: "POST",
      body: JSON.stringify({ display_name: displayName ?? null, locale }),
    }),
  getProgress: (sessionId: string) =>
    request<SessionProgressOut>(`/api/progress/sessions/${sessionId}`),
  updateProgress: (
    sessionId: string,
    body: {
      module_id: string;
      status: "not_started" | "in_progress" | "completed";
      last_question_id?: string;
    },
  ) =>
    request(`/api/progress/sessions/${sessionId}`, {
      method: "PUT",
      body: JSON.stringify(body),
    }),
  submitQuiz: (
    quizId: string,
    answers: Array<{
      question_id: string;
      selected_option_id?: string;
      written_answer?: string;
    }>,
    sessionId?: string | null,
  ) =>
    request<QuizSubmitResult>(`/api/quizzes/${quizId}/submit`, {
      method: "POST",
      body: JSON.stringify({ session_id: sessionId ?? null, answers }),
    }),
};
