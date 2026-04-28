# Split e Join

# método join() é usado para juntar elementos de uma 
# lista em uma string, usando um separador especificado.

# Criando uma lista de palavras
palavras = ["Olá", "mundo", "Python"]

# Usando join() para juntar as palavras com um espaço como separador
frase = " ".join(palavras)
print(frase)  # Output: Olá mundo Python

# método split() é usado para dividir uma string em uma lista,
# usando um separador especificado.

# Criando uma string de frutas separadas por vírgula
texto = 'Olá, mundo, Python'

# Usando split() para dividir a string em uma lista usando a vírgula como separador
texto_split = texto.split(', ')
print(texto_split)  # Output: ['Olá', 'mundo', 'Python']

# O método split() pode ser usado sem argumentos para dividir a string em palavras,
#  usando espaços como separadores
texto_split_espaco = texto.split()
print(texto_split_espaco)  # Output: ['Olá,', 'mundo,', 'Python']

# O método split() também pode ser usado para dividir uma string em linhas usando
#  o caractere de nova linha (\n) como separador
texto_multilinha = "Olá\nmundo\nPython"
texto_split_linhas = texto_multilinha.split('\n')
print(texto_split_linhas)  # Output: ['Olá', 'mundo', 'Python']

# o split é o contrário do join, ou seja, enquanto o join junta elementos 
# de uma lista em uma string, o split divide uma string em uma lista.