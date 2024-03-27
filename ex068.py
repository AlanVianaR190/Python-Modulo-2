from random import randint

com = randint(1,5)
cont = 0

print("---"*5,"Jogo do par ou impar","---"*5)

while True:
    play = int(input("Digite um numero de 1 a 5: "))
    op = str(input("Par[P] ou Impar[I]: ")).upper().strip()[0]

    while op not in ("P","I"):
        print("OPÇÃO INVALIDA")
        op = str(input("Par[P] ou Impar[I]: ")).upper().strip()[0]

    soma=com+play

    #condição se opção for PAR
    if op in "P":

        if soma % 2 == 0:
            print("GANHOU!")
            print(f"Jogador [{play}] x [{com}] Maquina ")
            cont += 1

        else:
            print("PERDEU!")
            print(f"Jogador [{play}] x [{com}] Maquina ")
            break

    #condição se opção for IMPAR
    if op in "I":

        if soma % 2 == 0:
            print("PERDEU")
            print(f"Jogador [{play}] x [{com}] Maquina ")
            break

        else:
            print("GANHOU!")
            print(f"Jogador [{play}] x [{com}] Maquina ")
            cont += 1

    print("---"*10)

print("FIM")
print(f"Voce ganhou {cont} vezes.")