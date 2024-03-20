mais=0
menos=0

for c in range(1,5):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))

    #Condição para pegar o mais pesado
    if c == 1 or peso > mais:
        mais = peso
        pesado = c

    #Condição para pegar o mais leve
    if c == 1 or peso < menos:
        menos = peso
        leve = c

print(f"O mais pesado foi {mais}kg")
print(f"O menos pesado foi o {menos}kg")

