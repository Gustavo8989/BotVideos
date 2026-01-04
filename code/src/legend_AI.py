import whisper 
import time 


modelo = whisper.load_model("base")

resposta = modelo.transcribe("corte_final.mp4")
print(resposta)

