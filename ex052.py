n = int(input("Digite um numero: "))
t = 0
for c in range(1, 1+n):
    if n % c == 0:
        t = t + 1
        print("\033[33m", end=" ")
    else:
        print("\033[31m", end=" ")
    print(f"{c}", end="")
print(f"\n\033[mO numero {n} foi divisivel {t}")
if t == 2:
    print("E PRIMO!")
else:
    print("Não e PRIMO")