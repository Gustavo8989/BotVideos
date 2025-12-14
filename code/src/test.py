import speech_recognition as sr


r = sr.Recognizer() 

print("Diga alguma coisa")
audio = r.listen("teste_audio.mp4") 
text = r.recognize_google(audio, language="pt-BR") 
