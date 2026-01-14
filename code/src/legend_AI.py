import whisper 
import time 
import re 

with open('text_legend.txt','r',encoding='utf-8') as text:
    text = text.read() 


lista = text.split()
letras = r'[^a-zA-Z\u00C0-\u017F]'

apenas_letras = []

for item in lista:
    itens_filtrados = re.sub(letras,'',item)
    apenas_letras.append(itens_filtrados)

ponteiro = 0
partes_legenda = [[]] 
print(len(apenas_letras))

while len(apenas_letras) > ponteiro:
    partes_legenda.append(apenas_letras[ponteiro])
    ponteiro += 13

print(partes_legenda)    
