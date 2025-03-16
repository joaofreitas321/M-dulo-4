"""
Tens um array com o número de pessoas transportadas nas viagens de um autocarro. 
Por exemplo: viagen=numpy.array([20,10,25,35,4]).Faz um programa que calcule e mostre:
"""
import numpy as np

viagem = np.array([20,10,25,35,4])
#Número total de pessoas transportadas 
total_pessoas = np.sum(viagem)
print(f"Número total de pessoas transportadas: {total_pessoas}")
#A média de pessoas transportadas
media_pessoas = total_pessoas / len(viagem)
print(f"A média de pessoas transportadas é {media_pessoas}")
#O maior número de pessoas transportadas numa viagem
max_pessoas = np.max(viagem)
print(f"O maior número de pessoas transportadas numa viagem é {max_pessoas}")
#O menor número de pessoas transportadas numa viagem
min_pessoas = np.min(viagem)
print(f"O menor número de pessoas transportadas numa viagem é {min_pessoas}")
#O número de viagens com mais pessoas que a média
viagens_acima_media = np.sum(viagem > media_pessoas)
print(f"O número de viagens com mais pessoas que a média é {viagens_acima_media}")