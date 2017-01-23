from math import log
from sys import argv
from tree import *


base = 256
freq = {}
acum = 0


def frequencia(texto): 
    """Calcula a frequencia da aparicao de cada caractere no texto e armazena no set 'freq'"""
    for c in texto:
        x = freq.get(c) or 0
        freq.update({c: x+1})
    

def entropy(texto):
    frequencia(texto)
    # p eh a probabilidade de massa
    acum = 0
    for i in freq:
        p = float(freq[i]) / float(len(texto))
        acum += p * log(p, base)
    return -acum


texto_orig = open(argv[1], 'rb').read()

freq = {}
entropy_orig = entropy(texto_orig)

l = []
for i in freq:
    l.append(N(i, freq[i]))

l.sort()
arvore = huffmann(l)
array = bitarray()

for i in texto_orig:
    array += arvore[i]

texto_zip = array.tobytes()

freq = {}
entropy_zip = entropy(texto_zip)

open('saida_zip', 'wb').write(texto_zip)


print("Entropia do texto original: " + str(entropy_orig))
print("Entropia do texto compactado: " + str(entropy_zip))