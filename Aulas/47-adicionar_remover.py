# Adicionando e removendo elementos de um dicionário

# Criando um dicionário
meu_dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3'
}
print(meu_dicionario)

# Adicionando um novo par chave-valor
meu_dicionario['chave4'] = 'valor4'
print(meu_dicionario)

# Removendo um par chave-valor usando del
del meu_dicionario['chave2']
print(meu_dicionario)

# Removendo um par chave-valor usando pop() - retorna o valor removido
valor_removido = meu_dicionario.pop('chave3')
print(f'Valor removido: {valor_removido}')
print(meu_dicionario)

# Limpando o dicionário usando clear()
meu_dicionario.clear()
print(meu_dicionario)  # dicionário vazio

# update() - método para atualizar um dicionário com outro dicionário 
# ou com pares chave-valor

novo_dicionario = {
    'chave5': 'valor5',
    'chave6': 'valor6'
}
meu_dicionario.update(novo_dicionario)
print(meu_dicionario)

# Atualizando um valor existente
meu_dicionario['chave5'] = 'novo_valor5'
print(meu_dicionario)

# diferença entre del, clear e pop()
# del - remove um par chave-valor específico do dicionário
# clear - remove todos os pares chave-valor do dicionário, deixando-o vazio
# pop - remove um par chave-valor específico do dicionário e retorna o valor removido

