# Tuplas em Python

# Estrutura de dados imutável, ou seja, não pode ser alterada após a criação
# Utilizada para armazenar múltiplos itens em uma única variável

# estrutura
# tupla = (item1, item2, item3, ...)

# Criando uma tupla
minha_tupla = (1, 2, 3, 'quatro', 'cinco')
print(minha_tupla)

# unpacking de tupla
a, b, c, d, e = minha_tupla
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # quatro
print(e)  # cinco

# Acessando elementos da tupla
print(minha_tupla[0])  # 1
print(minha_tupla[3])  # quatro

# Tuplas são imutáveis, então não podemos alterar seus elementos
# minha_tupla[0] = 10  # Isso causará um erro

# metodo count() - conta quantas vezes um elemento aparece na tupla
print(minha_tupla.count(2))  # 1
print(minha_tupla.count('quatro'))  # 1

# metodo index() - retorna o índice da primeira ocorrência de um elemento
print(minha_tupla.index(3))  # 2
print(minha_tupla.index('cinco'))  # 4

