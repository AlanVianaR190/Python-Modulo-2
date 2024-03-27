num = cont = 1

while True:
    num = int(input("Digite um numero para ver sua taboada (numero negativo encerra): "))

    if num < 0:
        break

    while cont < 10:
        print(f"{num:02d} x {cont} = {num * cont}")
        cont += 1

    # colocando o contador fora do 2º laço para zerar a contagem
    cont = 1

    print("---"*10)
print("FIM")