# Operador Ternário
# O operador ternário é uma forma concisa de escrever 
# uma expressão condicional em Python. Ele tem a seguinte sintaxe:

# valor_se_verdadeiro if condição else valor_se_falso

# Exemplo 1
entrada = input('Você quer entrar ou sair? ')
mensagem = 'Você entrou no sistema!' if entrada == 'entrar' \
    else 'Você saiu do sistema!' if entrada == 'sair' \
    else 'Você não digitou nem entrar nem sair!'
print(mensagem)

# Exemplo 2
numero = int(input('Digite um número: '))
resultado = 'O número é positivo!' if numero > 0 else 'O número é negativo!'
print(resultado)