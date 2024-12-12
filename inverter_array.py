"""Programa para inverter um array de nomes com 5 elementos"""
import numpy as np

NR_ELEMENTOS = 5

nomes = np.empty(NR_ELEMENTOS,dtype="U20")

for i in range(NR_ELEMENTOS):
    nomes[i] = input("Introduza o nome:")

nomes_invertidos = np.empty(NR_ELEMENTOS,dtype="U20")

k = NR_ELEMENTOS - 1

for i in range(NR_ELEMENTOS):
    nomes_invertidos[k] = nomes[i]
    k = k - 1

print(nomes,nomes_invertidos)    