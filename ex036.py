val_Cas = float(input("Digite aqui o valor da casa: R$"))
sal_Com = float(input("Digite aqui o salario do comprador: R$"))
quant_ano = int(input("Digite a quantidade de anos que pretende para efetuar o pagamento: "))

#metodo lambda p dividir o valor da casa em prestações
pres_Cas = lambda x, y: x / (y * 12)
prestacao = pres_Cas(val_Cas,quant_ano)
print(f"O valor da prestação de R${prestacao:.2f}")
print()

#Variavel para calcular a taxa
tax_pre = lambda x: (x * 30) /100
taxa = tax_pre(sal_Com)


if prestacao >= taxa:
    print(f"Ultrapassa 30% do salario do comprador que e de R${taxa:.2f}")
    print("Emprestimo negado")
else:
    print(f"Não ultrapassa 30% do salario do comprador que e de R${taxa:.2f}")
    print("Emprestimo Concedido")