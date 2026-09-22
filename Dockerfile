# ==============================================================================
# Production-Ready, Security-Optimized Dockerfile for Python Flask
# ==============================================================================

# 1. Base Image: Use official minimal Python slim image (Debian-based)
FROM python:3.11-slim

# 2. Environment Configurations
# - PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files to disk
# - PYTHONUNBUFFERED: Ensures real-time stdout and stderr output without buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# 3. Security: Create an unprivileged non-root user and group
# Running containers as root is a critical security vulnerability
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/bash -m appuser

# 4. Set dedicated working directory
WORKDIR /app

# 5. Dependency Layer Caching: Copy only requirements first
# Docker caches this layer; pip install only re-runs if requirements.txt changes
COPY requirements.txt .

# 6. Install dependencies without caching pip packages to keep image lightweight
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy application source code and adjust ownership
COPY . /app
RUN chown -R appuser:appgroup /app

# 8. Switch from root to non-root user
USER appuser

# 9. Expose application port
EXPOSE 5000

# 10. Container Health Check: Native Python check avoiding extra dependencies (like curl)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# 11. Production WSGI Server: Run Gunicorn with 2 workers and 2 threads
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
