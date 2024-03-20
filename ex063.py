cont = 3

t1 = 0    #primeiro termo
t2 = 1    #segundo termo
t3 = 0    #terceiro termo

quant = int(input("Quantos numeros voce quer mostrar da seq. FIBONACCI: "))
print(f"{t1} > {t2} > ",end=" ")

while cont <= quant:
    t3 = t1 + t2
    print(f"{t3} > ",end=" ")
    t1 = t2   #esta variavel passara a ter o valor da t2
    t2 = t3   #esta variavel passara a ter o valor da t3
    cont += 1
print("Fim")

