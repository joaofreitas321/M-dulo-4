contar = 0

email = input("Introduza o email:")
palavra_passe = input("Introduza a senha:")

if len(palavra_passe) >= 8:
    contar = contar + 1

if palavra_passe not in email:
    contar = contar + 1

for L in palavra_passe:
    if L >= 'a' and L <= 'z':
        contar = contar + 1
        break
for L in palavra_passe:
    if L >= 'A' and L <= 'Z':
        contar = contar + 1
        break

for L in palavra_passe:
    if L >= '0' and L <= '9':
        contar = contar + 1
        break
