print(14 % 4)
print(5 % 5)
print(10 % 1)

print(True> False)
print(True< False)
print(0>1)
print(1>0)

kilometros= float(input("Entre com o valor em Km:"))
milhas= float(input("Entre com o valor em milhas:"))

milhas_to_kilometros= milhas * 1.61
kilometros_to_milhas= kilometros/1.61

print(milhas,"milhas equivale a",round(milhas_to_kilometros,2),"kilometros")
print(kilometros,"kilometros equivale a",round(kilometros_to_milhas,2),"milhas")
