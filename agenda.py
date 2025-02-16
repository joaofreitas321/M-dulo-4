"""
Programa para gerir uma agenda de contactos. Cada contacto deve ter um nome
email e telefone.
A agenda deve permitir:
1. Aidicionar
2. Listar todos
3. Procurar
4. Apagar
5. Terminar
Utilize arrays para implementar as estruturas de dados.
"""
import numpy as np
#Estruturas de dados
MAX_ITEMS = 100

def Adicionar(nomes,emails,telefones,n_contactos):
    print("#"*30)
    print("## Adicionar contacto ##")
    print("#"*30)
    if n_contactos == MAX_ITEMS:
        print("A agenda de contactos está cheia!")
        return n_contactos
    nomes[n_contactos] = input("Nome:")
    emails[n_contactos] = input("Email:")
    telefones[n_contactos] = input("Telefone:")
    n_contactos += 1
    return n_contactos
    
def Listartodos(nomes,emails,telefones,n_contactos):
    print("#"*60)
    print("## Listar contactos ",end="")
    print(" "*38,end="")
    print("##")
    print("#"*60)
    for i in range(n_contactos):
        print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #")

def Procurar(nomes,emails,telefones,n_contactos):
    print("#"*60)
    print("## Procurar contactos ",end="")
    print(" "*39,end="")
    print("##")
    print("#"*60)
    procurar_nome = input("Introduza o nome do contacto:")
    for i in range(n_contactos):
        if procurar_nome in nomes[i]:
            print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #") 

def Apagar(nomes,emails,telefones,n_contactos):
    print("#"*60)
    print("## Apagar contactos ",end="")
    print(" "*39,end="")
    print("##")
    print("#"*60)
    procurar_nome = input("Introduza o nome do contacto:")
    for i in range(n_contactos):
        if procurar_nome in nomes[i]:
            print(f"# {nomes[i]} \t {emails[i]} \t {telefones[i]} \t #")
            op = input("Tem a certeza que pretende apagar este contacto? (s/n)")
            if op in 'sS':
                for k in range(i,n_contactos):
                    if k == MAX_ITEMS-1: #evita erro de ultrapassar limite do array 
                        break
                    nomes[k] = nomes[k+1]
                    emails[k] = emails[k+1]
                    telefones[k] = telefones[k+1]
                n_contactos -= 1
    return n_contactos                

def Editar(nomes,emails,telefones,n_contactos):
    """Função pesquisa um contacto pelo nome e permite alterar os dados"""
    #pedir o nome ao utilizador
    nome = input("QUal o nome do conracto a editar:")
    #percorrer o array dos nomes
    for i in range(n_contactos):
        #encontra o nome e permite alterar os dados
        if nome in nomes[i]:
            print(f"dados do contacto: {nomes[i]} - {emails[i]} - {telefones[i]}")
            op = input("Pretende editar estes dados? (S/N)")
            if op.lower()!="s":
                continue
            #editar os dados
            novo_nome = input("Introduza o novo nome ou deixa em branco para não alterar:")
            novo_email = input("Introduza o novo email ou deixe em branco para não alterar:")
            novo_telefone = input("Introduza o novo telefone ou deixe em branco para não alterar")
            if novo_nome.strip()!="":
                nomes[i] = novo_nome.strip()
            if novo_email.strip()!="":
                emails[i] = novo_email.strip()
            if novo_telefone.strip()!="":
                telefones[i] = novo_telefone.strip()    

def Menu():
    n_contactos = 0
    nomes = np.empty(MAX_ITEMS,dtype="U50")
    emails = np.empty(MAX_ITEMS,dtype="U50")
    telefones = np.empty(MAX_ITEMS,dtype="U50")
    op = 0
    while op != 6:
        print("1.Adicionar\2.Listar\3.Procurar\4.Apagar\5.Editar\6.Terminar")
        op = int(input("Opção:"))
        if op == 1:
            n_contactos = Adicionar(nomes,emails,telefones,n_contactos)
        elif op == 2:
            Listartodos(nomes,emails,telefones,n_contactos)
        elif op == 3:
            Procurar(nomes,emails,telefones,n_contactos)
        elif op == 4:
           n_contactos = Apagar(nomes,emails,telefones,n_contactos)
        elif op == 5:
            Editar(nomes,emails,telefones,n_contactos)   
        elif op == 6:
            break
        else:
            print("Opção não existe.")    


if __name__=="__main__":
    Menu()