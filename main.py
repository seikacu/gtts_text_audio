from gtts import gTTS


# pip install gTTS
tts = gTTS('Привет!', lang='ru')
tts.save('hello.mp3')