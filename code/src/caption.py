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
duracao = 5
legenda = []
duracao_video = video.duration

with open('text_legend.txt','r',encoding='utf-8') as text:
    text = text.read()

lista = text.split()
letras = r'[^a-zA-Z\u00C0-\u017F]'



sub = SubRipFile()
for i,frase in enumerate(texto,start=1):
    legend = SubRipItem(
        index=i,
        start=SubRipTime(0,0,tempo_inicial,0),
        end=SubRipTime(0,0,tempo_inicial+duracao,0),
        text=frase
    )
    sub.append(legend)
    tempo_inicial += duracao


for texto in sub:
    txt_clip = (TextClip(
                font=None,
                text=texto.text,
                color="Orange",
                font_size = 25,
                method='label')
                ).with_position(("center")).with_start(texto.start.seconds).with_duration(texto.end.seconds - texto.start.seconds)

video_final = CompositeVideoClip([video,txt_clip])
video_final.write_videofile("Teste videos com legenda.mp4",codec="libx264")

#xlTUwuVtqUOkL6gVAQCvZGXMmhZ16shAZXFfFpGe


'''     Modelo para legenda
1
00:00:01,000 --> 00:00:04,000
Olá, bem-vindo ao tutorial.

2
00:00:04,500 --> 00:00:08,000
Hoje vamos aprender sobre Python.
'''
