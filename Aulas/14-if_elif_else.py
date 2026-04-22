# If /    elif   / else
# se / senão se / senão

entrada= input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Você não digitou nem entrar nem sair!')

# Exemplo 2
numero = int(input('Digite um número: '))
if numero > 0:
    print('O número é positivo!')
elif numero < 0:
    print('O número é negativo!')
else:
    print('O número é zero!')

