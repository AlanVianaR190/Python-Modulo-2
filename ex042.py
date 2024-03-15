a = float(input("Digite o primeiro comprimento da reta: "))
b = float(input("Digite o segundo comprimento da reta: "))
c = float(input("Digite o terceiro comprimento da reta: "))

#Condição para saber se e possivel formar um trinagulo
if a+b>c and a+c>b and b+c>a:
    print("E possivel fazer um triangulo:")

    #condição para saber qual tipo de triangulo pode ser formado
    if a == b and b == c and c == a:
        print("EQUILATERO")

    elif a == b or b == c or c == a:
        print("ISOSCELES")

    elif a != b and b != c and c != a:
        print("ESCALENO")

else:
    print("Não e possivel formar um triangulo!")