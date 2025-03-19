tipo = input("Digite o tipo de número que deseja imprimir (par ou impar): ")

# Imprime os números pares ou ímpares de 1 a 10
for i in range(1, 11):
    if tipo == "par" and i % 2 == 0:
        print(i)
    elif tipo == "impar" and i % 2 != 0:
        print(i)

# Verifica números divisíveis por 3 e 5 entre 1 e 110
for i in range(1, 111):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "é divisível por 3 e 5")
    elif i % 3 == 0:
        print(i, "é divisível por 3")
    elif i % 5 == 0:
        print(i, "é divisível por 5")

