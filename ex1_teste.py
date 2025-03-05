import numpy as np

nomes = input("Nomes:")
tempos = input("Tempos:")

pilotos = np.array(nomes.split(","))
voltas = np.array(tempos.split(","))

i = 0

while i < 5:
    if int(voltas[i]) < 0:
        voltas[i] = int(input("..."))
    else:
        i = i + 1

posicao_melhor = 0
posicao_pior = 0

for i in range(5):
    if int(voltas[i]) < int(voltas[posicao_melhor]):
        posicao_melhor = i
    if int(voltas[i]) > int(voltas[posicao_pior]):
        posicao_pior = i

diferenca = int(voltas[posicao_pior]) - int(voltas[posicao_melhor])
print("Primeiro",pilotos[posicao_melhor])
print("Último", pilotos[posicao_pior])
print("Diferença", diferenca)

for i in range(5):
    print(pilotos[i], voltas[i])