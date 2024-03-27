while True:
    valor_saque = int(input("Digite o valor a ser sacado (ou 0 para sair): R$"))

    if valor_saque == 0:
        print("Programa encerrado.")
        break

    cedulas_50 = valor_saque // 50
    valor_saque %= 50

    cedulas_20 = valor_saque // 20
    valor_saque %= 20

    cedulas_10 = valor_saque // 10
    valor_saque %= 10

    cedulas_1 = valor_saque

    print(f"Serão entregues:")
    print(f"{cedulas_50} cédulas de R$50")
    print(f"{cedulas_20} cédulas de R$20")
    print(f"{cedulas_10} cédulas de R$10")
    print(f"{cedulas_1} cédulas de R$1")

