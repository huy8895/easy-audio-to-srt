FROM python:3.10

WORKDIR /workspace

# Cài ffmpeg và các Python package cần thiết
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --upgrade pip && \
    pip install setuptools-rust translate-toolkit googletrans openai-whisper flask

# Copy file Flask server vào image
COPY app.py /workspace/app.py

# Mở cổng 5000 cho webserver
EXPOSE 5000

# Khởi động Flask app
CMD ["python", "app.py"]
