# For com enumerate

# A função enumerate() é utilizada para obter o índice e o valor de 
# cada item em uma lista ou iterável.

# Estrutura:
# for indice, item in enumerate(lista):
    # repetir o código para cada item da lista, utilizando o indice e o item

lista = ['a', 'b', 'c', 'd']

for indice, item in enumerate(lista):
    print(f"Índice: {indice}, Item: {item}")

# For com enumerate e start
for indice, item in enumerate(lista, start=1):
    print(f"Índice: {indice}, Item: {item}")

# For com enumerate e start negativo
for indice, item in enumerate(lista, start=-1):
    print(f"Índice: {indice}, Item: {item}")

# For com enumerate e start negativo e step
for indice, item in enumerate(lista, start=-1):
    print(f"Índice: {indice}, Item: {item}")
