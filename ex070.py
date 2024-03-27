acum = cont = barat = caros = 0
nmbarat = " "

while True:
    nome = str(input("Digite o nome do produto: ")).strip()
    preco = int(input("Digite o preço do produto: R$ "))

    #
    if preco > 1000:
        caros += 1

    #
    if cont == 1 or preco < barat:
        barat = preco
        nmbarat = nome

    #
    cont += 1
    acum += preco

    op = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    while op not in("S","N"):
        print("OPÇÃO INVALIDA")
        op = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

    if op in "N":
        break

print(f"O total gasto na compra e R${acum:.2f}")
print(f"Teve {caros} produtos que custam mais que R$1000,00")
print(f"O produto mais barato foi o {nmbarat} que custa R${barat:.2f}")
print("FIM")