# Para o audio e video não ficar indo para o github vou fazer um sisema de upload e download 
import boto3 

s3 = boto3.client('s3')

BUCKET_NAME_AUDIO = "fileaudiobot"
FILE_PATH_AUDIO = "fileaudiobot"
S3_OBJECT_NAME_AUDIO = "3 fatos sobre o mar.mp3"

BUCKET_NAME_VIDEO = "filevideosbot"
FILE_PATH_VIDEO = "filevideosbot"
S3_OBJECT_NAME_VIDEO = "corte_final.mp4"

pergunta = str(input("Você quer fazer download do audio ou do video? "))
if pergunta.lower() == "audio":
    s3.download_file(BUCKET_NAME_AUDIO,S3_OBJECT_NAME_AUDIO,FILE_PATH_AUDIO)
elif pergunta.lower() == "video":
     s3.download_file(BUCKET_NAME_VIDEO,S3_OBJECT_NAME_VIDEO,FILE_PATH_VIDEO)
