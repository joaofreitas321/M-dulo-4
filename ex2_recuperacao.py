n_telefone = input("Introduza o seu número de telefone:")

valido = True

if len(n_telefone) != 9:
    print("Deve ter 9 dígitos.")
    valido = True

for L in n_telefone:
    if L.isdigit() == False:
        print("Deve ter só digitos numéricos.")
        valido = False

if n_telefone[0] != "9" or n_telefone[1] not in "1236":
    print("Deve começar por 91,92,93 ou 96.")
    valido = False

contar = 0
for posicao in range(2,len(n_telefone)):
    if n_telefone[posicao] == "0":
        contar = contar + 1
if contar == 7:
    print("Não pode ser um número só de 0.")
    valido = False

if valido == True:
    print("Válido.")