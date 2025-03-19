



#Tabuada de 0 a 10

# Solicita ao usuário um valor entre 1 e 10
numero = int(input("Digite um número entre 1 e 10: "))

# Verifica se o número está no intervalo correto
if 1 <= numero <= 10:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido! Digite um número entre 1 e 10.")




