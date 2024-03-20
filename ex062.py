cont = 1

pri = int(input("Digite o primeiro termo da PA: "))
raz = int(input("Digite a razão da PA: "))

ter = pri

#variavel para guardar o valor total de termos
total = 0

#variavel para mostrar os 10 primeiros termos & mostrar mais termos
plus = 10

while plus != 0:
    total = total + plus

    while cont <= total:
        print(ter, end=" -> ")
        ter += raz
        cont = cont + 1

    print("Pause")
    plus = int(input("Quantos termos voce quer que moste a mais: "))

print(f"Programa encerado com {total} termos mostrados")
