# variavel do contador
cont=0

#variavel acumulador
acum=0

print("A soma entre todos os números que são múltiplos de três de 1 até 500.")
for num in range(1, 501, 2):

    if num % 3 == 0:

        # capturar a quantidade (contador)
        cont = cont + 1

        # capturar a soma (acumulador)
        acum = acum + num

print(f"Quantidade de numeros mostrados {cont}")
print(f"O valor de todos os numeros somados e {acum}")