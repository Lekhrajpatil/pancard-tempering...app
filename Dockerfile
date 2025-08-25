# Railway-friendly Dockerfile for Python 3.11

# 1) Base image
FROM python:3.11-slim

# 2) System dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-venv \
       python3-pip \
       build-essential \
       libssl-dev \
       libffi-dev \
       git \
    && rm -rf /var/lib/apt/lists/*

# Helpful defaults
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 3) Project files
WORKDIR /app
COPY . /app

# 4) Create virtual environment at /opt/venv
RUN python -m venv /opt/venv

# 5) Activate venv, upgrade pip, install requirements
# Use explicit path to pip inside venv to avoid activation issues
RUN /opt/venv/bin/pip install --upgrade pip \
    && if [ -f requirements.txt ]; then /opt/venv/bin/pip install -r requirements.txt; fi

# 6) Add venv to PATH for all subsequent commands & runtime
ENV PATH="/opt/venv/bin:$PATH"

# 7) Expose port 8000 (Railway can map this to $PORT)
EXPOSE 8000

# 8) Run the main app
CMD ["python", "app.py"]
