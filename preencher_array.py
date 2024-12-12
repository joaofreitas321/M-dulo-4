"""
Programa para preencher um array com 10 elementos em que cada elemento é o 
dobro do valor do índice da sua posição
"""
import numpy as np

numeros = np.empty(10)

for i in range(10):
    numeros[i] = i * 2

print(numeros)    