#URNA ELETRONICA
# Votação
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

while True:
    print("As opções são:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    voto = int(input("Entre com o seu voto (ou 6 para encerrar): "))

    if voto == 6:
        break
    elif voto in votos:
        votos[voto] += 1
    else:
        print("Voto inválido!")

# Exibe os resultados
total_votos = sum(votos.values())
porcentagem_nulo = (votos[4] / total_votos) * 100 if total_votos else 0
porcentagem_branco = (votos[5] / total_votos) * 100 if total_votos else 0

# Identificar o vencedor
vencedor = max(votos[1:4], key=lambda x: votos[x])

print("\nResultados da votação:")
print(f"Votos Jair Rodrigues: {votos[1]}")
print(f"Votos Carlos Luz: {votos[2]}")
print(f"Votos Neves Rocha: {votos[3]}")
print(f"Votos Nulos: {votos[4]}")
print(f"Votos Brancos: {votos[5]}")
print(f"Porcentagem de votos nulos: {porcentagem_nulo:.2f}%")
print(f"Porcentagem de votos brancos: {porcentagem_branco:.2f}%")
print(f"Candidato vencedor: {['Jair Rodrigues', 'Carlos Luz', 'Neves Rocha'][vencedor-1]}")

