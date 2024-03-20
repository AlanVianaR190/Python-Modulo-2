op = "S"
cont = acum = maior = menor = 0

while op in "S":
    num = int(input("Digite um valor: "))
    op = str(input("Quer digitar mais um valor (s/n)? ")).upper().strip()[0]
    acum += num
    cont += 1

    #
    if cont == 1 or num < menor:
        menor = num

    #
    if cont == 1 or num > maior:
        maior = num

media = acum / cont

print(f"Foram mostrados {cont} e eles somados e {acum} a media entre eles e {media:.1f}")
print(f"O maior numero é {maior} e o menor numero é {menor}")


