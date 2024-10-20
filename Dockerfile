FROM python:3.12.7-slim

# Install system dependencies (curl) and clean up afterward
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install poetry \
# Install Poetry using curl
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to PATH (this ensures poetry is available globally)
ENV PATH="/root/.local/bin:$PATH"

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Set up the working directory inside the container
WORKDIR /app

# Copy poetry project files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock ./

# Install dependencies via poetry (no dev dependencies)
RUN poetry install --no-dev

# Copy the FastAPI app code to the container
COPY --link . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
