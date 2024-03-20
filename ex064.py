#versão melhorada
cont = acum = 0

num = int(input("Digite um numero (999 para parar): "))

while num != 999:
    acum += num
    cont += 1
    num = int(input("Digite um numero (999 para parar): "))
print(f"A soma entre estes numeros e de {acum} & foram mostrados {cont} numeros")
