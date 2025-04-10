FROM python:3.10-slim

WORKDIR /workspace

# Cài ffmpeg và các dependency cần thiết cho pip package có build (Rust, gcc...)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    libffi-dev \
    libsndfile1 \
    build-essential \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài pip packages
RUN pip install --upgrade pip && \
    pip install setuptools-rust && \
    pip install -U openai-whisper

# Preload model tiny để không cần tải lại khi chạy container
RUN python -c "import whisper; whisper.load_model('tiny')"

CMD ["bash"]
