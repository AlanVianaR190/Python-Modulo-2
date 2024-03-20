t = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for n in range(1,11):
    pa = t + (n - 1) * r
    print(pa, end="->")
print("Fim")

