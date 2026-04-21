# poliformismo de concatenação
# O operador + tem um comportamento diferente dependendo do tipo de dado
# Se for números, ele realiza a adição
# Se for strings, ele realiza a concatenação

# Exemplo de concatenação de strings
nome = 'João'
sobrenome = 'Silva'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

# Exemplo de adição de números
num1 = 10
num2 = 20
soma = num1 + num2
print(soma)

# Exemplo de concatenação de strings e números
idade = 30
mensagem = 'A idade de ' + nome + ' é ' + str(idade) + ' anos.'
print(mensagem)

# concatenação de strings usando f-strings (forma mais moderna e legível)
mensagem_f = f'A idade de {nome} é {idade} anos.'
print(mensagem_f)

# com o operador de multiplicação, o comportamento também é 
# diferente dependendo do tipo de dado
# Se for números, ele realiza a multiplicação
multiplicacao = 5 * 3
print(multiplicacao)

# Se for strings, ele realiza a repetição
# Exemplo de repetição de strings
repeticao = 'Olá ' * 3
print(repeticao)

