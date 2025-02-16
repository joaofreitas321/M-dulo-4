"""
Programa que vai ler dois nomes completos e vê pelo último nome 
se são da mesma família ou não.
Versão hacker: Dois nomes são familiares se um dos dois últimos nomes 
forem iguais por qualquer ordem (ultimo=penultimo,ultimo=ultimo,
penultimo=penultimo).
"""

def Familiares(A,B) -> bool:
    """Função que devolve true se os nomes são de familiares"""
    nomesA = A.split(" ") #lista com os nomes
    nomesB = B.split(" ") #lista com os nomes
    #verificar se os últimos nomes são iguais
    if nomesA[len(nomesA)-1] == nomesB[len(nomesB)-1]:
        return True
    #verificar se os dois últimos nomes são iguais
    for i in nomesA[1:]:
        for k in nomesB[1:]:
            if i == k:
                return True
    return False     


nomeA = input("Introduza o seu nome completo")
nomeB = input("Introduza o seu nome completo")

print(Familiares(nomeA,nomeB))