import playsound
import os
import random
import time
from gtts import gTTS


def response(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1,1000000)
    audio_file = 'audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)



time.sleep(1)
while 1:
    ask = input("Enter what you want: ")
    response(ask)
