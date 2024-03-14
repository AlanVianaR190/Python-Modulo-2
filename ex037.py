n = int(input("Digite um numero inteiro: "))
print(f"Digite 1 para converter o numero {n} em em BINARIO >>>")
print(f"Digite 2 para converter o numero {n} em em OCTAL >>>")
print(f"Digite 3 para converter o numero {n} em em HEXADECIMAL >>>")

op = int(input("Opção: "))

#
if op == 1:
    convercao = bin(n)[2:]
    print(f"Este numero convertido em BINARIO")
    print(f"{convercao}")
elif op == 2:
    convercao = oct(n)[2:]
    print(f"Este numero convertido em OCTAL é")
    print(f"{convercao}")
elif op == 3:
    convercao = hex(n)[2:]
    print(f"Este numero convertido em HEXADECIMAL é")
    print(f"{convercao}")