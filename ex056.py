mulheres = 0
velhoNome = ""
velhoIdade = 0
idades = 0

for c in range(1, 5):
    nome = str(input("Digite o nome: ")).upper().strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo (m - masculino / f - feminino): ")).upper().strip()

    idades += idade

    #condição p pegar o mais velho
    if c == 1 and sexo in "M" or idade > velhoIdade and sexo in "M":
        velhoNome = nome
        velhoIdade = idade

    #condição p pegar quantas mulheres tem menos de 20 anos
    if sexo in "fF" and idade < 20:
        mulheres += 1

media = idades / 4

print(f"A media de idade desse grupo e de {media:.1f}")
print(f"O mais velho e {velhoNome} com {velhoIdade}")
print(f"Neste grupo tem {mulheres} mulheres com menos de 20 anos")