# Importar as bibliotecas 
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from pysrt import SubRipFile, SubRipItem, SubRipTime
from elevenlabs.client import ElevenLabs
import assemblyai as aii 
import cohere
import boto3

# Pegar a cheve APi
# MUDAR ISSO DEPOIS para .env
with open("key.txt",'r') as key:
    key = key.read()
with open("key_voice.txt", 'r') as voice:
    voice = voice.read()
with open("key_aii.txt",'r') as legend:
    legend = legend.read()

# API da Voz 
ELEVENLABS_API_KEY = voice 
s3 = boto3.client('s3') # AWS
# Conectando com a chave

co = cohere.ClientV2(key)
menssage = [] # Usado para salvar as conversas so usuarios, não esta sendo usado atualmente
user_input = input("Digite o tema do seu texto: ")
messages=[{"role": "user", "content": user_input}]
response = co.chat(
    model="command-a-03-2025", 
    messages=[{"role":"user", "content":"xbox360"}]
)
bot_reply = response.message.content[0].text
text_clear = bot_reply.replace('**','')

# Salvando o texto para transformar em legenda 
salve = input("Você quer salvar o seu texto?").lower()
if salve == "sim":
    with open("text_legend.txt",'w',encoding='utf-8') as legend:
        legend.write(text_clear)
    print("Legenda criada com sucesso.. :)")

print("Transformando em audio...")

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
    print("Finalizado... ")

text_to_speech(text_clear)
