"""
Programa para ler as notas de 10 alunos, calcular e mostrar a média das notas e por fim mostrar
as notas que são superiores à média
"""

import numpy as np
#constante com o valor do nº de alunos
NR_ALUNOS = 10

#definir o array para as notas
notas = np.zeros(NR_ALUNOS)

#ler as notas
for n in range(NR_ALUNOS):
    notas[n] = int(input("Nota:"))
print(notas)    