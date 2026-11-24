/** Safe, user-facing API errors — never surface raw transport bodies. */

export class ApiError extends Error {
  readonly status: number;

  constructor(status: number, message = "request_failed") {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }

  get isUnauthorized(): boolean {
    return this.status === 401 || this.status === 403;
  }
}
