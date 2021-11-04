from flask import Flask, jsonify, send_file, request, abort
import os
import time
import malaya_speech
from pydub import AudioSegment
from io import BytesIO
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['POST'])
def speakSinglish(text):
    if not request.json or not 'text' in request.json: abort(400)
    mp3 = BytesIO()
    AudioSegment((np.iinfo(np.int16).max * vocoder(tacotron.predict(request.json["text"])["universal-output"])).astype(np.int16).tobytes(), frame_rate=22050, sample_width=2, channels=1).export(mp3, format="mp3", bitrate="320k")
    mp3.seek(0)
    return send_file(mp3, as_attachment=True, attachment_filename='test.mp3', mimetype='audio/mpeg')


if __name__ == '__main__':
    tacotron = malaya_speech.tts.tacotron2(model='female-singlish')
    vocoder = malaya_speech.vocoder.melgan(model='universal-1024')
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
