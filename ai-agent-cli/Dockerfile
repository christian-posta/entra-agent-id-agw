# AI Agent CLI Container Image
# Multi-stage build for smaller final image

# -----------------------------------------------------------------------------
# Build stage
# -----------------------------------------------------------------------------
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------
# Runtime stage
# -----------------------------------------------------------------------------
FROM python:3.12-slim AS runtime

# Labels
LABEL maintainer="your-email@example.com" \
    description="AI Agent CLI with Microsoft Entra authentication and MCP tools" \
    version="0.1.0"

# Create non-root user for security
RUN groupadd --gid 1000 agent \
    && useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home agent

# Set working directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY agent_cli/ ./agent_cli/

# Copy config file if needed (optional - can be mounted at runtime)
# COPY agentgateway_config.yaml ./

# Create directory for config persistence
RUN mkdir -p /home/agent/.config/ai-agent-cli \
    && chown -R agent:agent /home/agent/.config

# Switch to non-root user
USER agent

# Set Python environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Health check (optional - checks if Python and module are importable)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from agent_cli import __version__; print(__version__)" || exit 1

# Default command - run the interactive CLI
ENTRYPOINT ["python", "-m", "agent_cli.main"]
CMD ["run"]

