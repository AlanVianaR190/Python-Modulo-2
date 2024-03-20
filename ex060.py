num = int(input("Digite um numero para calcular seu FATORIAL: "))
c = num
f = 1

while c > 0:
    print(f" {c} ", end=" ")
    print(" x " if c > 1 else " = ", end=" ")
    f = f * c
    c = c - 1

print(f" {f} ")

