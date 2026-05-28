from flask import Flask, request, send_file
from gtts import gTTS
import tempfile
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data['text']
    # สร้างเสียงภาษาไทย (gTTS ใช้ Google Translate TTS)
    tts = gTTS(text=text, lang='th', slow=False)
    # บันทึกลงไฟล์ชั่วคราว
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tmp_path = f.name
    tts.save(tmp_path)
    return send_file(tmp_path, mimetype='audio/mpeg', as_attachment=True, download_name='audio.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
