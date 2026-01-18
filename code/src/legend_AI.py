import whisper 
import time 
import re 

with open('text_legend.txt','r',encoding='utf-8') as text:
    text = text.read() 


lista = text.split()
letras = r'[^a-zA-Z\u00C0-\u017F]'

apenas_letras = []
inicio = 0  
fim = 13
for item in lista:
    itens_filtrados = re.sub(letras,'',item)
    apenas_letras.append(itens_filtrados)

partes_legenda = {} 

for c in range(len(apenas_letras)//13):
    partes_legenda = {f"Parte{c}":apenas_letras[inicio:fim]}
    inicio = fim 
    fim += 13
    print(partes_legenda)

