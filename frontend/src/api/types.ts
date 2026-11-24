export type LocalizedText = { nl: string; en: string };

export type Attribution = {
  source_name: string;
  source_url: string | null;
  note: LocalizedText;
  knhb_illustration_placeholder: boolean;
  translation_needed: boolean;
};

export type FurtherReading = {
  title: LocalizedText;
  url: string;
  attribution: Attribution;
};

export type ModuleStub = {
  id: string;
  kind: "field" | "indoor" | "shared";
  title: LocalizedText;
  summary: LocalizedText;
  learning_objectives: LocalizedText[];
  instruction_outline: LocalizedText[];
  quiz_id: string | null;
  further_reading: FurtherReading[];
  order: number;
};

export type QuizOption = { id: string; text: LocalizedText };

export type QuizQuestion = {
  id: string;
  type: "multiple_choice" | "written";
  prompt: LocalizedText;
  options: QuizOption[] | null;
};

export type Quiz = {
  id: string;
  title: LocalizedText;
  questions: QuizQuestion[];
};

export type CourseOutline = {
  id: string;
  title: LocalizedText;
  description: LocalizedText;
  modules: ModuleStub[];
  quizzes: Record<string, Quiz>;
  attributions: Attribution[];
};

export type SessionOut = {
  id: string;
  display_name: string | null;
  locale: string;
  created_at: string;
  updated_at: string;
  expires_at: string;
};

export type SessionCreatedOut = SessionOut & {
  /** Present only when the API exposes bearer tokens (dev). Prefer httpOnly cookie. */
  access_token: string | null;
};

export type ProgressOut = {
  module_id: string;
  status: "not_started" | "in_progress" | "completed" | string;
  quiz_score: number | null;
  quiz_total: number | null;
  last_question_id: string | null;
  completed_at: string | null;
  updated_at: string;
};

export type SessionProgressOut = {
  session: SessionOut;
  progress: ProgressOut[];
};

export type QuizAnswerResult = {
  question_id: string;
  correct: boolean;
  explanation: LocalizedText;
  visualization_hint: string | null;
  correct_option_id: string | null;
};

export type QuizSubmitResult = {
  quiz_id: string;
  score: number;
  total: number;
  results: QuizAnswerResult[];
  progress_saved: boolean;
};
