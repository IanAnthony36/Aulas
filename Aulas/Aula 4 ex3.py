# Códigos ANSI para cores
VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"  # Resetar cor padrão do terminal

# Entrada do usuário
numero = int(input("Digite um número: "))  
eh_primo = True  

# Verifica se o número é menor que 2
if numero < 2:
    eh_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{VERMELHO}{numero} não é um número primo.{RESET}")
            eh_primo = False
            break

if eh_primo:
    print(f"{VERDE}{numero} é um número primo.{RESET}")
    