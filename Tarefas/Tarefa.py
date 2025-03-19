#Ordem crescente e Decrescente

# Solicita os valores ao usuário
primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o último valor: "))

# Verifica se a contagem será crescente ou decrescente
if ultimo > primeiro:
    for i in range(primeiro, ultimo + 1):
        print(i)
else:
    for i in range(primeiro, ultimo - 1, -1):
        print(i)






