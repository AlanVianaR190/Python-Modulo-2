n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
op = 0

#Laço de repetição while
while op != 5:
    print("---"*10)
    print("Digite [1] p SOMAR\n"
                 "Digite [2] p MULTIPLICAR\n"
                 "Digite [3] p MAIOR\n"
                 "Digite [4] p NOVOS NUMEROS\n"
                 "Digite [5] p SAIR")

    op=int(input("Digite sua opção: "))

    #
    if op == 1:
        print(f"O numero {n1} somado ao numero {n2} e igual {n1 + n2}!")

    elif op == 2:
        print(f"O numero {n1} multiplicado ao numero {n2} e igual {n1 * n2}!")

    elif op == 3:

        if n1 > n2:
            print(f"O numero {n1} e maior que o {n2}")

        elif n1 < n2:
            print(f"O numero {n1} e menor que o {n2}")

        else:
            print(f"O numero {n1} e igual ao {n2}")

    elif op == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))

    else:
        print("Opção Invalida")

print("Encerando Programa. Volte sempre!")
