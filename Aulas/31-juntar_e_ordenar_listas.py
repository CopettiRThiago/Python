# Juntar listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Juntando as listas usando o operador +
lista_junta = lista1 + lista2
print(f"Lista juntada usando +: {lista_junta}")  # Output: Lista juntada usando +: [1, 2, 3, 4, 5, 6]

# Juntando as listas usando o método extend()
lista1.extend(lista2)
print(f"Lista1 após usar extend: {lista1}")  # Output: Lista1

# Juntando as listas usando o método append() em um loop
lista3 = []
for item in lista1:
    lista3.append(item)
print(f"Lista3 após usar append em loop: {lista3}")  # Output: Lista3 após usar append em loop: [1, 2, 3, 4, 5, 6]

# ordenar listas

lista_desordenada = [5, 2, 9, 1, 5, 6]

# Ordenando a lista usando o método sort()
lista_desordenada.sort()
print(f"Lista ordenada usando sort(): {lista_desordenada}")  # Output:

# Lista ordenada usando sort(): [1, 2, 5, 5, 6, 9]
# Ordenando a lista usando a função sorted()
lista_desordenada = [5, 2, 9, 1, 5, 6]  # Recriando a lista desordenada
lista_ordenada = sorted(lista_desordenada)
print(f"Lista ordenada usando sorted(): {lista_ordenada}")  # Output: Lista ordenada usando sorted(): [1, 2, 5, 5, 6, 9]

# a função sorted() retorna uma nova lista ordenada, enquanto o método sort() ordena a lista original.