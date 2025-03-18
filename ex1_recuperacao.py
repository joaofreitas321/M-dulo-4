import numpy as np

meses_2022 = np.array(['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'])
mortes_2022 = np.array([42,49,44,55,57,66,49,82,66,71,55,32])

for posicao in range(len(meses_2022)):
    if meses_2022[posicao] == "Março":
        print(mortes_2022[posicao])
        break

soma = 0
for n in mortes_2022:
    soma = soma + n
print(soma)

media = soma / 365
print(media)

trimestre = mortes_2022[0] + mortes_2022[1] + mortes_2022[2]
print(trimestre)

maior = mortes_2022[0]
posicao_maior = 0

for posicao in range(len(mortes_2022)):
    if mortes_2022[posicao] > maior:
        maior = mortes_2022[posicao]
        posicao_maior = posicao

print(meses_2022[posicao_maior])

#Contar e mostrar quantos meses tem o número de mortes superior à média
contar = 0

for valor in mortes_2022:
    if valor > media:
        contar = contar + 1
print(contar)