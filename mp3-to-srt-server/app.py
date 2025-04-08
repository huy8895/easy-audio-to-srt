from flask import Flask, request, jsonify, send_file
import os
import subprocess
import uuid

app = Flask(__name__)

WORK_DIR = "/workspace"

@app.route('/')
def home():
    return "🎙️ SlowScribe API is running!", 200

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'world')
    return jsonify({'message': f'Hello, {name}! 👋'})

@app.route('/slowdown', methods=['POST'])
def slowdown():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    speed = request.form.get('speed', default='0.8')  # lấy tốc độ nếu có, mặc định 0.8

    try:
        speed_float = float(speed)
        if not 0.5 <= speed_float <= 1.0:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Speed must be a number between 0.5 and 1.0'}), 400

    uid = uuid.uuid4().hex[:8]
    input_path = os.path.join(WORK_DIR, f"{uid}_{file.filename}")
    output_path = os.path.join(WORK_DIR, f"slowed_{uid}.mp3")

    file.save(input_path)

    try:
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-filter:a", f"atempo={speed}",
            "-vn", output_path,
            "-y"
        ], check=True)
    except subprocess.CalledProcessError:
        return jsonify({'error': 'Audio slowdown failed'}), 500

    if os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    else:
        return jsonify({'error': 'Processed file not found'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
