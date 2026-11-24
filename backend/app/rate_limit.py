"""Lightweight in-process sliding-window rate limiter (single-worker v0).

Multi-worker / multi-replica deployments should put rate limits at the edge
or switch to a shared store — each process has its own limiter state.
"""

from __future__ import annotations

import threading
import time
from collections import defaultdict, deque

from fastapi import HTTPException, Request, status

from app.config import settings


class SlidingWindowRateLimiter:
    def __init__(self) -> None:
        self._hits: dict[str, deque[float]] = defaultdict(deque)
        self._lock = threading.Lock()

    def check(self, bucket: str, limit: int, window_seconds: int) -> None:
        now = time.monotonic()
        cutoff = now - window_seconds
        with self._lock:
            queue = self._hits[bucket]
            while queue and queue[0] < cutoff:
                queue.popleft()
            if len(queue) >= limit:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Try again shortly.",
                    headers={"Retry-After": str(window_seconds)},
                )
            queue.append(now)

    def reset(self) -> None:
        with self._lock:
            self._hits.clear()


limiter = SlidingWindowRateLimiter()


def client_ip(request: Request) -> str:
    """Identify the client for rate limiting.

    By default uses the direct peer address only. When COURSE_TRUST_PROXY is
    true, uses the *rightmost* X-Forwarded-For hop (closest to our proxy),
    which is harder to spoof than the leftmost client-controlled value.
    """
    peer = request.client.host if request.client and request.client.host else None

    if settings.trust_proxy:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            parts = [p.strip() for p in forwarded.split(",") if p.strip()]
            if parts:
                # Rightmost entry is typically appended by the nearest proxy.
                return parts[-1]

    if peer:
        return peer
    # Avoid a single shared global bucket when peer is missing.
    return f"no-peer:{id(request)}"


def enforce_session_create_limit(request: Request) -> None:
    limiter.check(
        f"session-create:{client_ip(request)}",
        settings.rate_limit_session_create,
        settings.rate_limit_window_seconds,
    )


def enforce_quiz_submit_limit(request: Request) -> None:
    limiter.check(
        f"quiz-submit:{client_ip(request)}",
        settings.rate_limit_quiz_submit,
        settings.rate_limit_window_seconds,
    )
