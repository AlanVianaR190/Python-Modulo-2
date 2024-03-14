from datetime import date
nasc = int(input("Digite o ano de nascimento: "))

#variavel com comando date.today().year para pegar ano atual
atual = date.today().year
idad = atual - nasc
print(f"Sua idade e de {idad}")

#
if idad == 18:
    print("Voce esta na idade de se alistar.")
elif idad < 18:
    print("Voce não esta na idade de se alistar.")

    # variavel p pegar a quantidade de anos que ainda falta
    saldo = 18 - idad

    print(f"Ainda falta {saldo} anos, seu alistamento sera em {atual + saldo}")
else:
    print("Voce ja passou da idade de se alistar.")

    # variavel p pegar a quantidade de anos que passou
    saldo = idad - 18

    print(f"Ja passou {saldo} anos do prazo, deveria ter se alistado em {atual - saldo}")
