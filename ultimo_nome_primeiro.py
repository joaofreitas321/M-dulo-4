"""
Programa para ler um nome e mostrar o nome no formato: ultimo, primeiro
segundo ..."""

def AlterarNome(nome) -> str:
    #separa os nomes
    nomes = nome.split(" ")
    #verificar se é só um nome
    if len(nomes) == 1:
        return nome
    #criar uma string com o ulitmo nome e,
    nome_alterado = nomes[len(nomes)-1] + ", "
    #juntar na string os restantes nomes
    for n in nomes[:len(nomes)-1]:
        nome_alterado = nome_alterado + n + " "
    return nome_alterado.strip()    

def main():
    nome = input("Introduza o seu nome completo:")
    nome_alterado = AlterarNome(nome)
    print(nome_alterado)

if __name__=="__main__":
    main()    