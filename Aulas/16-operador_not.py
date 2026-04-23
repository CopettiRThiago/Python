# Operador NOT
# O operador NOT é um operador lógico que inverte o valor de uma 
# expressão booleana. Ele é representado pela palavra-chave "not" em Python. 
# O operador NOT é usado para negar uma condição ou para verificar se uma condição é falsa.

# Exemplo 1

print(not True)  # Saída: False
print(not False)  # Saída: True

# Exemplo 2

entrada = input('Você quer entrar ou sair? ')
if not (entrada == 'entrar' or entrada == 'sair'):
    print('Você não digitou nem entrar nem sair!')

# Exemplo 3
numero = int(input('Digite um número: '))
if not numero > 0:
    print('O número é negativo ou zero!')

