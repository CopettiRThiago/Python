# Interpolação de strings

# A interpolação de strings é uma técnica que permite inserir 
# valores de variáveis dentro de uma string de forma mais legível 
# e conveniente. Em Python, existem várias maneiras de realizar 
# a interpolação de strings, incluindo o uso do operador % (antigo),
#  o método str.format() e as f-strings (a partir do Python 3.6).

# str -> transformação de um valor em string
# %s - string
# %d e %i- inteiro
# %f - ponto flutuante
# x e X - hexadecimal

# Exemplo usando o operador %
nome = "Alice"
idade = 30
print("Meu nome é %s e eu tenho %d anos." % (nome, idade))

# Exemplo usando o método str.format()
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Exemplo usando f-strings
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Exemplo com hexadecimal

numero = 255
print("O número %d em hexadecimal é %x." % (numero, numero))
print(f"O número {numero} em hexadecimal é {numero:x}.")

