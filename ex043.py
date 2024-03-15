alt = float(input("Digite a altura (m): "))
pes = float(input("Digite o peso (kg): "))

#Calcular o indice de massa corporea
imc = pes / (alt * alt)
print(f"O IMC é {imc:.1f} é esta:")

#
if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25:
    print("PESO IDEAL")
elif imc >= 25 and imc < 30:
    print("SOBREPESO")
elif imc >= 30 and imc < 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MORBIDA")