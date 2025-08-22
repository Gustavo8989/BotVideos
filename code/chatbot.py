# Importar as bibliotecas 
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import assemblyai as aii 
import cohere
import boto3
import os 
import uuid 

# Pegar a cheve APi
# MUDAR ISSO DEPOIS para .env
with open("key.txt",'r') as key:
    key = key.read()
with open("key_voice.txt", 'r') as voice:
    voice = voice.read()
with open("key_aii.txt",'r') as legend:
    legend = legend.read()

'''load_dotenv(dotenv_path="bot_criar_videos/.env")
key = os.getenv("API_KEY_COHERE")
print(key)
'''

ELEVENLABS_API_KEY = voice 
s3 = boto3.client('s3')
# Conectando com sua chave
co = cohere.ClientV2(key)
menssage = [] # Usado para salvar as conversas so usuarios, não esta sendo usado atualmente
user_input = input("Digite: ")
messages=[{"role": "user", "content": user_input}]
response = co.chat(
    model="command-a-03-2025", 
    messages=messages
)
bot_reply = response.message.content[0].text
menssage.append({"role":"asistant","content":bot_reply})

# Parte da voz
elevenLabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)
def text_to_speech(text:str) -> str:
    response = elevenLabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", #Código da voz
        output_format="mp3_22050_32",
        text = text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )
    save_file_path = f"{user_input}.mp3"
    with open(save_file_path,"wb") as f:
        for c in response:
            if c:
                f.write(c)
    BUCKET_NAME = "fileaudiobot"
    FILE_PATH = save_file_path
    S3_OBJECT_NAME = save_file_path
    response = s3.list_buckets()
    s3.upload_file(FILE_PATH,BUCKET_NAME,S3_OBJECT_NAME)

text_to_speech()