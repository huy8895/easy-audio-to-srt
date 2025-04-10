FROM python:3.10

WORKDIR /workspace

# Cài ffmpeg và pip packages cần thiết cho Whisper
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --upgrade pip && \
    pip install setuptools-rust && \
    pip install -U openai-whisper && \
    python -c "import whisper; whisper.load_model('tiny'); whisper.load_model('small')"
