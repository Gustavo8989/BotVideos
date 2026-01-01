# Para o audio e video não ficar indo para o github vou fazer um sisema de upload e download 
from tqdm import tqdm
import boto3 

print("-"*30)
file_name_video = input("Digite o nome do video? ")
file_name_audio = input("Digite o nome do audio? ")

s3 = boto3.client('s3')

# Bucket Audio
BUCKET_NAME_AUDIO = "fileaudiobot"
FILE_PATH_AUDIO = "3 fatos sobre o mar.mp3"
S3_OBJECT_NAME_AUDIO = "3 fatos sobre o mar.mp3"

#Bucket Video
BUCKET_NAME_VIDEO = "filevideosbot"
FILE_PATH_VIDEO = "Minecraft Parkour Gameplay No Copyright.mp4"
S3_OBJECT_NAME_VIDEO = "Minecraft Parkour Gameplay No Copyright.mp4"

question = input("Quer fazer Download e Upload [D/U]: ")

if question.lower() == "d":
    download_file = str(input("Você quer fazer download do audio ou do video? "))
    if download_file.lower() == "audio":
        s3.download_file(BUCKET_NAME_AUDIO,S3_OBJECT_NAME_AUDIO,FILE_PATH_AUDIO)
        print("Download feito com sucesso")
    elif download_file.lower() == "video":
        s3.download_file(BUCKET_NAME_VIDEO,S3_OBJECT_NAME_VIDEO,FILE_PATH_VIDEO)
        print("Download feito com sucesso")

elif question.lower() == "u":
    upload_question = str(input("Você quer fazer upload do audio ou video: "))
    if upload_question.lower() == "audio":
        s3.upload_file(FILE_PATH_AUDIO,BUCKET_NAME_AUDIO,S3_OBJECT_NAME_AUDIO)
        print("Upload feito com sucesso")
    elif upload_question.lower() == "video":
        s3.upload_file(FILE_PATH_VIDEO,BUCKET_NAME_VIDEO,S3_OBJECT_NAME_VIDEO)
        print("Upload feito com sucesso")