# Adivinhação de números
import random

# Número secreto
numero_secreto = random.randint(1, 100)

# Adivinhação
while True:
    palpite = int(input("Adivinhe um número entre 1 e 100: "))
    
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        print("Tente novamente!")



