FROM python:3.10

WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --upgrade pip && \
    pip install setuptools-rust translate-toolkit googletrans openai-whisper && \
    python -c 'import whisper; whisper.load_model("tiny"); whisper.load_model("small")'
