# Fatiamento de strings
'''
O fatiamento de strings é uma técnica que permite acessar partes 
específicas de uma string usando índices. A sintaxe básica para 
fatiar uma string é: string[início:fim:passo]

- início: O índice onde o fatiamento começa (inclusivo). Se omitido, o padrão é 0.

- fim: O índice onde o fatiamento termina (exclusivo). Se omitido, o padrão é o comprimento da string.

- passo: O intervalo entre os caracteres a serem fatiados. Se omitido, o padrão é 1.

Obs.: o final não é incluído no resultado do fatiamento, ou seja, 
o fatiamento inclui os caracteres do índice de início até o índice de fim - 1.
'''

# Exemplo de fatiamento de strings
texto = "Olá, mundo!"
print(texto[0:5])  # Saída: Olá, m
print(texto[7:12]) # Saída: mundo
print(texto[:5])   # Saída: Olá, m
print(texto[::2])  # Saída: Oá udo
print(texto[1::2])  # Saída: l,mn!
print(texto[::-1])  # Saída: !odnum ,álO (string invertida)

