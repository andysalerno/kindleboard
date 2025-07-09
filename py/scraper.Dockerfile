FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster dependency management
RUN pip install uv

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-dev

# Install Playwright browsers
RUN uvx playwright install chromium
RUN uvx playwright install-deps chromium

# Copy application files
COPY screenshot_webpage.py convert_img.py ./

# Set default environment variables
ENV OUTPUT_PATH=screenshot.png
ENV UPDATE_SECONDS=60
ENV URL=

# Run the screenshot script
CMD ["uv", "run", "python", "screenshot_webpage.py"]