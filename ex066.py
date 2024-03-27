num = cont = acum = 0

while True:
    num = int(input("Digite um numero: "))

    if num == 999:
        break

    cont += 1
    acum += num

print(f"Foram digitados {cont} numeros. E a soma entre eles e de {acum}")
