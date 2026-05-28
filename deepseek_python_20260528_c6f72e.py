# tts_service.py
from flask import Flask, request, send_file
import edge_tts, tempfile, os
app = Flask(__name__)
@app.route('/tts', methods=['POST'])
async def tts():
    data = request.get_json()
    communicate = edge_tts.Communicate(data['text'], "th-TH-PremwadeeNeural")
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tmp_path = f.name
    await communicate.save(tmp_path)
    return send_file(tmp_path, mimetype='audio/mpeg', as_attachment=True, download_name='audio.mp3')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)