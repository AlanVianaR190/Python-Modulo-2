c = 1
pri = int(input("Digite o primeiro termo da PA: "))
raz = int(input("Digite a razão da PA: "))

ter = pri

while c <= 10:
    print(ter, end="->")
    ter += raz
    c = c + 1
print("Fim")
