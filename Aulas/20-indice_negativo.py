# Índices negativos em strings
# Além dos índices positivos, as strings também suportam índices negativos.
# O índice -1 se refere ao último caractere da string, -2 ao penúltimo, e assim por diante.

# Exemplo de acesso a caracteres usando índices negativos

#Negativos -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#            O  L  Á  ,     M  U  N  D  O  !
# Índice:   0   1  2  3  4  5  6  7  8  9  10

# Exemplo 1
texto = "Olá, mundo!"
print(texto[-1])  # Imprime '!'
print(texto[-2])  # Imprime 'o'
print(texto[-3])  # Imprime 'd'
print(texto[-7])  # Imprime 'm'

# Exemplo 2

email = 'texto@gmail.com'
nome = 'João Silva'

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres') # retorna 15
print('Primeiro Caractere ' + email[0]) # retorna 't'
print('Último Caractere ' + email[-1])  # retorna 'm'
print('Servidor do email ' + email[6:11]) # retorna 'gmail'
print('Servidor do email ' + email[email.index('@')+1:email.index('.')]) # retorna 'gmail'