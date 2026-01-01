import speech_recognition as sr
from pydub import AudioSegment


r = sr.Recognizer() 

with sr.AudioFile('teste_termo.wav') as source:
    audio_data = r.record(source)
    try:
        texto = r.recognize_google(audio_data,language='pt-BR')
    except sr.RequestError as e:
        print("Erro encontrado {e}")
    

#audio = AudioSegment.from_mp3("teste_termo.mp3")
#audio.export("teste_termo.wav",format="wav")
print(texto)