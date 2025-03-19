#Cálculo de Rentabilidade de Poupança
# Solicita o valor inicial
P = float(input("Digite o valor inicial que deseja investir: "))

# Taxa de juros
i = 0.5 / 100

# Calcula o montante mês a mês
for n in range(1, 13):
    M = P * (1 + i) ** n
    print(f"Mês {n}: R${M:.2f}")

    






