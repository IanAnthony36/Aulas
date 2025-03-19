for variavel in range(1):  # Substitua `sequencia` por um valor válido
    for i in range(10):
        print("O valor de i é atualmente:", i)
        
        for j in range(1, 6):
            for k in range(2, 8, 3):
                print("O valor de k é:", k)

                # Cálculo de potências de 2
                for expo in range(1, 6):
                    power = 2 ** expo
                    print(f"2 elevado a {expo} é {power}")

                   
print("Comando break")
for i in range(1, 6):
    if i == 3:
        break  # Sai do loop quando i for 3
    print("Dentro do loop:", i)
print("Fora do loop.")  # Executa após sair do loop

print("\nComando continue")
for i in range(1, 6):
    if i == 3:
        continue  # Pula a iteração quando i for 3
    print("Dentro do loop:", i)
print("Fora do loop.")  # Executa após o loop terminar

