from random import randint
from time import sleep

#tupla com as opção
opc = ("PEDRA","PAPEL","TESOURA")

#Função <randint> do modulo <random> para maquina escolher aleatoriamente algum item da tupla
com = randint(0,2)

print("Vamos jogar JOKENPO >>>")
player = int(input("Digite [0] para PEDRA\n"
                 "Digite [1] para PAPEL\n"
                 "Digite [2] para TESOURA\n"
                 "Opção:"))

print("JO"),sleep(1)
print("KEN"),sleep(1)
print("PO"),sleep(1)

#Opção da maquina
print(f"Eu escolhi {opc[com]}")

#Opção do jogador
print(f"Voce escolheu {opc[player]}")

#pedra
if com == 0:

    if player == 0:
        print("Deu EMPATE")

    elif player == 1:
        print("Voce GANHOU")

    elif player == 2:
        print("Voce PERDEU")

    else:
        print("Não VALEU")

#papel
elif com == 1:

    if player == 0:
        print("Voce PERDEU")

    elif player == 1:
        print("Deu EMPATE")

    elif player == 2:
        print("Voce GANHOU")

    else:
        print("Não VALEU")

#tesoura
elif com == 2:

    if player == 0:
        print("Voce GANHOU")

    elif player == 1:
        print("Voce PERDEU")

    elif player == 2:
        print("Deu EMPATE")

    else:
        print("Não VALEU")

print("Fui")


""""#pedra
if com == 0 and player == 1:
    print("Voce GANHOU!")
elif com == 0 and player == 2:
    print("Voce PERDEU")
elif com == 0 and player == 0:
    print("Deu EMPATE")
#papel
elif com == 1 and player == 2:
    print("Voce GANHOU!")
elif com == 1 and player == 0:
    print("Voce PERDEU")
elif com == 1 and player == 1:
    print("Deu EMPATE")
#tesoura
elif com == 2 and player == 0:
    print("Voce GANHOU!")
elif com == 2 and player == 1:
    print("Voce PERDEU")
elif com == 2 and player == 2:
    print("Deu EMPATE")
else:
    print("OPÇÃO INVALIDA")"""
