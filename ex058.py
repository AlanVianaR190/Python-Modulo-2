'''from random import randint
maquina=randint(1,5)
tentos=1
print("Advinhe o numero em que estou pensando!")
numero=int(input("Digite um numero de 1 a 5: "))
while numero!=maquina:
    numero=int(input("Errou, tente de novo: "))
    tentos+=1
print(f"Acertou, estava pensando em {maquina}!")
print(f"Precisou de {tentos} tentativas")'''

from random import randint
maquina = randint(1,10)
acerto = False
tento = 0
print("Adivinhe em que numero estou pensando de 1 ate 10!?")
while not acerto:
    num = int(input("Diga qual numero: "))
    tento += 1
    if maquina == num:
        acerto = True
print(f"Exato. Acertou com {tento} tentativas")

