FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

# Use /app as the working directory
WORKDIR /app

# Compile bytecode and avoid symlinks
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# ---------- Layer 1: dependencies ----------
COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-install-project

# ---------- Layer 2: application code ----------
COPY . .

# Install application dependencies in the virtual environment
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

CMD ["python", "main.py"]
