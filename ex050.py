#acumulador
acum = 0

for c in range(0, 6):
    n = int(input("Digite um numero: "))

    if n % 2 == 0:
      acum = acum + n

print(f"Os numeros pares somados e igual: {acum}")