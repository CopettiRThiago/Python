# Métodos de dicionários

# Criando um dicionário
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

# Método get() - Retorna o valor de uma chave, ou um valor padrão se a chave não existir
print(pessoa.get('nome'))  # Output: João

# Método keys() - Retorna uma lista de chaves do dicionário
print(pessoa.keys())  # Output: dict_keys(['nome', 'idade', 'cidade'])

# Método values() - Retorna uma lista de valores do dicionário
print(pessoa.values())  # Output: dict_values(['João', 30, 'São Paulo'])

# Método items() - Retorna uma lista de tuplas (chave, valor) do dicionário
print(pessoa.items())  # Output: dict_items([('nome', 'João'), ('idade', 30), ('cidade', 'São Paulo')])

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))