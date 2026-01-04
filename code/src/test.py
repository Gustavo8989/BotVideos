import speech_recognition as sr
from pydub import AudioSegment
from datetime import timedelta 
from moviepy.video.io.VideoFileClip import VideoFileClip

r = sr.Recognizer() 

'''with sr.AudioFile('teste_termo.wav') as source:
    audio_data = r.record(source)
    try:
        texto = r.recognize_google(audio_data,language='pt-BR')
    except sr.RequestError as e:
        print("Erro encontrado {e}")
#audio = AudioSegment.from_mp3("teste_termo.mp3")
#audio.export("teste_termo.wav",format="wav")
print(texto)'''


'''with open("text_legend.txt",'r') as legend:
    legend = legend.read() 
print(legend)
'''

video = VideoFileClip("corte_final.mp4")
duracao = video.duration
inicio = 0
fim = 5

while duracao > fim:
    if fim > duracao:
        break 
    inicio = fim 
    fim += 5


total_legendas = duracao / 5 
print(total_legendas) 



# Ver quantas palavras a IA consegue "falar" em 5 segundo
# Faer uma variavel que sempre vai aumentando de 5 em 5 (laço) por exemplo 
'''
00:00:01,000 -> 00:00:05,000
    Teste 1 2 3 até onde vai 
00:00:05,000 -> 00:00:10,000
    De 5 em 5 vamos testando
'''
