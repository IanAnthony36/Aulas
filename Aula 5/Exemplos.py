lista_com_duplicatas = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7, 8, 5, 9]
lista_sem_duplicatas = []

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0)  # Remove o primeiro elemento da lista original
    if elemento not in lista_sem_duplicatas:  # Verifica se já está na lista sem duplicatas
        lista_sem_duplicatas.append(elemento)

print("A lista sem duplicatas é:", lista_sem_duplicatas)
