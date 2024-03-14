n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))

media = (n1+n2) / 2
print(f"Sua media é {media:.1f}")

if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")
