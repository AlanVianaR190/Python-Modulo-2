from datetime import date

ano = int(input("Digite o ano de nascimento do atleta: "))

#variavel p pegar a idade utilizando a função <.today().year> do modulo <datetime> subtraindo o ano de entrada
idade = date.today().year-ano

#
print(f"Com {idade} a categoria é:")

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SENIOR")
else:
    print("MASTER")