# For dentro de For

# Estrutura:
# for item in iterável:
    # for item2 in iterável2:
        # repetir o código para cada combinação de item e item2

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

for numero in lista1:
    for letra in lista2:
        print(f"Número: {numero}, Letra: {letra}")

# For dentro de For com dicionários
dicionario1 = {'x': 10, 'y': 20}
dicionario2 = {'a': 1, 'b': 2}
for chave1, valor1 in dicionario1.items():
    for chave2, valor2 in dicionario2.items():
        print(f"Chave1: {chave1}, Valor1: {valor1}, Chave2: {chave2}, Valor2: {valor2}")

