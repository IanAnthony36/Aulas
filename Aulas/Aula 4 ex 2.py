usuario_palavra = input("Entre com uma palavra: ")
usuario_palavra = usuario_palavra.upper()
for letra in usuario_palavra:
    if letra == "A":
        continue
    if letra == "E":
        continue
    if letra == "I":
        continue
    if letra == "O":
        continue
    if letra == "U":
        continue
    else:
        print(letra)


        usuario_palavra = input("Entre com uma palavra: ").upper()

for letra in usuario_palavra:
    if letra in "AEIOU":  
        continue
    print(letra, end="")  # O argumento end="" evita a quebra de linha

print()  # Apenas para garantir que o cursor pule para a próxima linha no final