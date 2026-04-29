# For com range

# Estrutura:

# for item in range(n):
    # repetir o código n vezes

for i in range(5):
    print(i)

# For com range e len()
lista = ['a', 'b', 'c', 'd']
for i in range(len(lista)):
    print(f"Índice: {i}, Item: {lista[i]}")

# For com range com step
for i in range(0, 10, 2):
    print(i)

# For com range com step negativo
for i in range(10, 0, -2):
    print(i)

# For com range com step negativo e sem o stop
for i in range(10, 0, -1):
    print(i)

# For com range com step negativo e sem o stop e sem o start
for i in range(10, 0, -1):
    print(i)

print("\n Utilizando a função range()")
for numero in range(5):
  print("Numero:", numero)