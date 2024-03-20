from datetime import date

#Variaveis de contador
maior = 0
menor = 0

for c in range(1,5):
    ano = int(input(f"Digite a idade da {c}ª pessoa: "))
    idade = date.today().year-ano
    print(f"A idade dela e {idade}")

    #
    if idade >= 18:
        maior += 1

    else:
        menor += 1

print(f"Tem {maior} pessoas que são de maior idade ")
print(f"Tem {menor} pessoas que não são de maior")
