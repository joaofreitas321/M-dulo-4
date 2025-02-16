"""Programa para inverter um array de nomes com 5 elementos"""
import numpy as np

NR_ELEMENTOS = 5

nomes = np.empty(NR_ELEMENTOS,dtype="U20")

for i in range(NR_ELEMENTOS):
    nomes[i] = input("Introduza o nome:")

k = NR_ELEMENTOS - 1

for i in range(NR_ELEMENTOS // 2):
    temp = nomes[i]
    nomes[i] = nomes[k]
    nomes[k] = temp
    k = k - 1
    
print(nomes)    