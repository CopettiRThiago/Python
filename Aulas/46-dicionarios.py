# Dicinoários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, o que significa que você pode alterar seus valores após a criação.
#  Em Python, os dicionários são criados usando chaves {} e os pares de 
# chave-valor são separados por dois pontos (:).

# Estrutura:

# dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

# Criando um dicionário
meu_dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3'
}
print(meu_dicionario)

# Acessando valores do dicionário usando as chaves
print(meu_dicionario['chave1'])  # valor1
print(meu_dicionario['chave2'])  # valor2
print(meu_dicionario['chave3'])  # valor3

# get() - método para acessar valores do dicionário, retorna None se a chave não existir
print(meu_dicionario.get('chave1'))  # valor1

