import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from io import BytesIO
import malaya_speech

tacotron = malaya_speech.tts.tacotron2(model='female-singlish')
vocoder = malaya_speech.vocoder.melgan(model='universal-1024')

mp3 = BytesIO()
AudioSegment((np.iinfo(np.int16).max * vocoder(tacotron.predict("Hello World, this is a test of a Singaporean accent. Currently we only have a female singlish accent but let's see how it goes.")["universal-output"])).astype(np.int16).tobytes(), frame_rate=22050, sample_width=2, channels=1).export(mp3, format="mp3", bitrate="320k")
mp3.seek(0)

print(mp3.read())
