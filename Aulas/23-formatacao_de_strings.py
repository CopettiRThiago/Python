# Formatação de strings

'''
:< - Alinhamento à esquerda
:> - Alinhamento à direita
:^ - Alinhamento ao centro
: - Especifica o preenchimento
.2f - Formata um número de ponto flutuante com 2 casas decimais
:+ - Exibe o sinal para números positivos e negativos
:, - Adiciona separadores de milhares
:_ - Substitui o espaço em branco por um caractere específico

'''

# Exemplo de formatação de strings
nome = "texto"
idade = 30
altura = 1.75
print(f"Nome: {nome:<10} | Idade: {idade:>3} | Altura: {altura:.2f}m")

# Exemplo de formatação com preenchimento
numero = 1234567.89
print(f"Número formatado: {numero:,.2f}")

# Exemplo de formatação com sinal
saldo = 1500.75
print(f"Saldo: {saldo:+.2f}")

# Exemplo de formatação com preenchimento personalizado
valor = 42
print(f"Valor formatado: {valor:_>10}")

# Exemplo de formatação com alinhamento ao centro
titulo = "Curso de Python"
print(f"{titulo:^30}")

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:-^10}.') # preenche com o simbolo escolhido
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

# conversion flags
print(f'{variavel!s}') # str()
print(f'{variavel!r}') # repr()
print(f'{variavel!a}') # ascii()

