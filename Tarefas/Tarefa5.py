import random  # Importa a biblioteca random

# Solicita ao usuário o número de lançamentos
quantidade = int(input("Quantas vezes você quer lançar a moeda? "))
caras = 0
coroas = 0

# Simulação dos lançamentos
for _ in range(quantidade):
    resultado = random.randint(0, 1)  # 0 para cara, 1 para coroa
    if resultado == 0:
        print("Cara")
        caras += 1
    else:
        print("Coroa")
        coroas += 1

print(f"Total de Caras: {caras}")
print(f"Total de Coroas: {coroas}")

