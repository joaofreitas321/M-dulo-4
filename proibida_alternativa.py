"""
Um programa que lê uma frase do utilizador e se tiver uma palavra
proibida mudar para uma palavra alternativa.
"""
import numpy as np

proibidas = np.array(["mau","pobre","infeliz","péssimo","feio",])
alternativas = np.array(["bom","rico","feliz","ótimo","bonito"])

frase = input("Introduza uma frase:")

for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase = frase.replace(proibidas[i],alternativas[i])

print(frase)