sexo = str(input("Digite o SEXO da pessoa (m - masculino / f - feminino): ")).upper().strip()

#Laço de repetição while caso a entrada não seja dentro dos parametros
while sexo not in("M","F"):
    print("OPÇÃO INVALIDA")
    sexo = str(input("Digite o sexo da pessoa (m - masculino / f - feminino): ")).upper().strip()
print("SEXO registrado com sucesso!")
