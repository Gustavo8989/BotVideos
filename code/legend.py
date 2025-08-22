from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip 
import whisper 
import time 

# Declarando o modelo / E o video 
model = whisper.load_model("base")
result = model.transcribe("corte_final.mp4",fp16=False)
result_text = result["text"].split()
atraso_palavra = 0.5
teste = ""
for c in result_text:
    time.sleep(atraso_palavra)
    teste = c

# Colocando a legenda no video
video = VideoFileClip("corte_final.mp4")
txt_clip = (TextClip(
            font=None,
            text=teste,
            color="Orange",
            font_size = 25,
            method='label'))

txt_clip = txt_clip.with_position(("center","bottom")).with_duration(video.duration)

video_final = CompositeVideoClip([video,txt_clip])
video_final.write_videofile("Teste videos com legenda.mp4",codec="libx264")