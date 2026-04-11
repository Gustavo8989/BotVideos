from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip  
from pysrt import SubRipFile, SubRipItem, SubRipTime
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import re               

video = VideoFileClip("corte_final.mp4")
tempo_inicial = 1
palavras_bloco = 8
duracao = 5
duracao_video = video.duration

with open('text_legend.txt','r',encoding='utf-8') as text:
    text = text.read()

lista = text.split()
letras = r'[^a-zA-Z\u00C0-\u017F]'

apenas_letras = [] 
texto = {}
inicio = 0 
fim = 13  
tempo = tempo_inicial
clips = [video]

for item in lista:
    itens_filtrados = re.sub(letras,'',item)
    apenas_letras.append(itens_filtrados) 

for c in range(len(apenas_letras)//13):
    parte_legenda = {f"Partes{c}":apenas_letras[inicio:fim]}
    inicio_seg = tempo  
    fim = tempo + duracao
    texto = ' '.join(parte_legenda[f"Partes{c}"])
    sub = SubRipFile()
    legend = SubRipItem(
        index=c,
        start=SubRipTime(0,0,tempo_inicial,0),
        end=SubRipTime(0,0,tempo_inicial+duracao,0),
        text=texto 
    )
    sub.append(legend)  

    txt_clip = (TextClip(
                font=None,
                text=texto,
                color="Black",
                font_size = 25,
                method='label')
                ).with_position(("center")).with_start(inicio).with_end(duracao_video)
    clips.append(txt_clip) 
    tempo_inicial += duracao
  

video_final = CompositeVideoClip(clips)
video_final.write_videofile("Teste videos com legenda.mp4",codec="libx264",audio_codec="aac")
print("Video salvo")


#xlTUwuVtqUOkL6gVAQCvZGXMmhZ16shAZXFfFpGe


'''     Modelo para legenda
1
00:00:01,000 --> 00:00:04,000
Olá, bem-vindo ao tutorial.

2
00:00:04,500 --> 00:00:08,000
Hoje vamos aprender sobre Python.
'''
