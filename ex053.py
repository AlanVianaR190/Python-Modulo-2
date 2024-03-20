esq = str(input("Digite uma frase: ")).upper().strip()

#A função <split> dividi a frase
palavra = esq.split()

#A função <join> junta tudo
juntar = ''.join(palavra)

#Variavel para ler de tras pra frente
inver = juntar[::-1]

print(f"O inverso de {juntar} e {inver}")

if inver == juntar:
    print("E um PALINDROMO")

else:
    print("Não e um PALINDROMO")
