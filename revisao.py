"""
Um programa para registar os nomes dos clientes que entraram numa loja num
determinado dia e o valor das compras de cada.
O programa deve mostrar o nome do cliente que fez a compra mais cara.
"""
import numpy as np

MAX_CLIENTES = 10

nomes = np.empty(MAX_CLIENTES,dtype="U50")
compras = np.empty(MAX_CLIENTES,dtype="f")

#array passado por referência
def LerDados(nomes_clientes,compras_clientes):
    n_clientes = int(input("Introduza quantos clientes entraram na loja?"))
    for i in range(n_clientes):
        nomes_clientes[i] = input("Introduza o nome:")
        compras_clientes[i] = input("Introduza o valor das compras:")

#função para mostrar o nome do melhor cliente
def MelhorCliente(nomes_clientes,compras_clientes):
    maior_compra = compras_clientes[0]
    posicao = 0
    #percorrer o array
    for i in range(MAX_CLIENTES):
        if maior_compra < compras_clientes[i]:
            #guardar o maior valor e a posição
            maior_compra = compras_clientes[i]
            posicao = i
    print(f"O melhor cliente foi {nomes_clientes[posicao]} que gastou {compras_clientes[posicao]}")        


LerDados(nomes,compras)
MelhorCliente(nomes,compras)