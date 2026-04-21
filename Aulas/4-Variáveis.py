# Variáveis são usadas para armazenar valores e podem ser 
# de diferentes tipos, como números, strings, listas, etc.
# Em Python, não é necessário declarar o tipo da variável,
# basta atribuir um valor a ela.
# PEP8 - iniciar o nome de uma variável com letra minúscula e usar 
# underscores para separar palavras

# Atribuição de uma variável

nome = 'Texto'
idade = 30

# Imprimindo o valor da variável
print(nome)
print(idade)

# Variáveis podem ser reatribuídas a outros valores
nome = 'Outro texto'
print(nome)

# input() é uma função que permite ao usuário inserir um valor, 
# que é armazenado em uma variável. O valor retornado por input() é sempre uma string,
# mesmo que o usuário digite um número.

nome_usuario = input('Digite seu nome: ')

# print() é uma função que exibe o valor de uma variável ou expressão
print('Olá, ' + nome_usuario + '!')
