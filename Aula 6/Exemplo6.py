cadastro = {}
while True:
    Nome = input("DIGITE O NOME COMPLETO:")
    if Nome == '':
        break

    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")

    cadastro[Nome] = {"Idade": idade, "cidade": cidade}

    print("Cadastro:")
    print(cadastro)
    for nome, dados in cadastro.items():
        print("-Nome:", nome)
        print("- Idade:", dados["idade"])
        print(" Cidade:",dados["cidade"])
