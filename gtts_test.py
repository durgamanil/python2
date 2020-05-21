from gtts import gTTS
import os 
tts = gTTS('onyx components and systems')
tts.save('hello.mp3')
os.system("hello.mp3") 