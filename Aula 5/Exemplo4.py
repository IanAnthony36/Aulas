minha_lista = [17,8, 10, 6, 2, 4]
trocado = True

while trocado:
    trocado = False
    for i in range(len(minha_lista) - 1):
        if minha_lista[i] > minha_lista[i + 1]:
            trocado = True
            minha_lista[i], minha_lista[i + 1] = \
            minha_lista[ i + 1], minha_lista[i]


print(minha_lista)