preco = float(input("Digite o valor da compra: R$"))

#Entrada de opção
op = int(input("Digite [1] a vista dinheiro/cheque\n"
      "Digite [2] a vista cartão\n"
      "Digite [3] 2x no cartão\n"
      "Digite [4] 3x ou mais no cartão\n"
      "Qual opção: "))

#Condição para dar o valor final
if op == 1:
    preco = preco - (preco * 0.10)

elif op == 2:
    preco = preco - (preco * 0.05)

elif op == 3:
    val = preco / 2
    print(f"O valor de cada parcela e de R${val:.2f}")

elif op == 4:
    preco = preco + (preco * 0.20)

    #Entrada e variavel para o parcelamento
    par = int(input("Digite a quantidade de vezes"))
    val=preco/par
    print(f"O valor de cada parcela e de R${val:.2f}")

else:
    print("OPÇÃO INVALIDA")
print(f"O valor total a ser pago e de R${preco:.2f}")