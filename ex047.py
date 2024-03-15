print("Os numeros pares de 1 ate 50 são:")

#Laço começando pelo numero 2 ate 51, pulando de dois em dois
for num in range(2, 51, 2):
    print(num, end= " ")
print()

#list comprehension
paresDe50 = [x for x in range(2, 51, 2)]

print(paresDe50)