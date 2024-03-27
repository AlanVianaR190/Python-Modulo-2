homens = mulheres = maiores = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = str(input("Digite o sexo da pessoa [M/F]: ")).upper().strip()[0]

    while sexo not in("M","F"):
        print("OPÇÃO INVALIDA")
        sexo = str(input("Digite o sexo da pessoa [M/F]: ")).upper().strip()[0]

    # condição para sexo feminino
    if sexo in "F":

        if idade >= 20:
            mulheres += 1

            #acumulador de maior de idade
            maiores += 1

    #condição para sexo masculino
    if sexo in "M":
        homens += 1

        #condição para acumular maior de idade
        if idade >= 18:
            maiores += 1

    op = str(input("Deseja cadastrar mais? [S/N]: ")).upper().strip()[0]
    while op not in("S","N"):
        print("OPÇÃO INVALIDA")
        op = str(input("Deseja cadastrar mais? [S/N]: ")).upper().strip()[0]

    if op == "N":
        break

print("PROGRAMA ENCERADO")
print(f"Foram cadastrados {maiores} pessoas 18+\n"
      f"Foram cadastrados {homens} homens\n"
      f"Foram cadastradas {mulheres} mulheres 20+")

