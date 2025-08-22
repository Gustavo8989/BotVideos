from moviepy import * 
from pytubefix import YouTube
import numpy as np 
import boto3 
import subprocess 
import tempfile
import os 
import math


s3 = boto3.client('s3')
BUCKET_NAME = "filevideosbot"
FILE_PATH = "filevideosbot"
S3_OBJECT_NAME = "Minecraft Parkour Gameplay No Copyright.mp4"

video = VideoFileClip("video1.mp4")
duracao = video.duration
começo = 0 
audio_final = AudioFileClip("3 fatos sobre o mar.mp3")
audio = audio_final.duration
audio = math.ceil(audio)
final = audio
clip_corte1 = video.subclipped(0,final) # Cortando parte do video 
corte_no_audio = clip_corte1.without_audio()
clip_corte1 = corte_no_audio.with_audio(audio_final)
clip_corte1.write_videofile("corte_final.mp4")

question_video = input("Você quer dowload de um videos? ")
if question_video.lower() == "sim":
    try:
        url = input("Digite a url do videos: ") 
        yt = YouTube(url)
        ys = yt.streams.filter(progressive=False,file_extension='mp4').get_by_resolution("1080p")
        ys.download(filename="video1.mp4")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

