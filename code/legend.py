from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip  
from pysrt import SubRipFile, SubRipItem, SubRipTime
import openai
import moviepy

video = VideoFileClip("corte_final.mp4")
tempo_inicial = 1 
duracao = 5
legenda = []
duracao_video = video.duration


with open('text_legend.txt','r',encoding='utf-8') as text_clear:
    text_clear = text_clear.read().splitlines()


sub = SubRipFile()
for i,frase in enumerate(text_clear,start=1):
    legend = SubRipItem(
        index=i,
        start=SubRipTime(0,0,tempo_inicial,0),
        end=SubRipTime(0,0,tempo_inicial+duracao,0),
        text=frase
    )
    sub.append(legend)
    tempo_inicial += duracao

# Melhorar o código 
range_numeros = [c for c in enumerate(sub)]
range_numeros = [i for i in range(len(range_numeros) - 1)]



for c in range_numeros:
    txt_clip = (TextClip(
                font=None,
                text=sub[c].text,
                color="Orange",
                font_size = 25,
                method='label')).with_position(("center","bottom")).with_duration(duracao_video)

video_final = CompositeVideoClip([video,txt_clip])
video_final.write_videofile("Teste videos com legenda.mp4",codec="libx264")


# https://json2video.com/
