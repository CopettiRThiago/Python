# For com dicionários

# Estrutura:
# for chave, valor in dicionario.items():
    # repetir o código para cada par de chave e valor do dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

# For com dicionários e keys()
for chave in dicionario.keys():
    print(f"Chave: {chave}")

# For com dicionários e values()
for valor in dicionario.values():
    print(f"Valor: {valor}")
