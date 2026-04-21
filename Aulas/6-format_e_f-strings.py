# métodos format() e f-strings

# método format()

nome = 'Maria'
idade = 30
mensagem = 'Olá, meu nome é {} e eu tenho {} anos.'.format(nome, idade)
print(mensagem)  # Output: Olá, meu nome é Maria e eu tenho 30 anos.

# f-strings (disponível a partir do Python 3.6)

nome = 'João'
idade = 25
mensagem = f'Olá, meu nome é {nome} e eu tenho {idade} anos.'
print(mensagem)  # Output: Olá, meu nome é João e eu tenho 25 anos.

# f-strings também permitem expressões dentro das chaves

a = 5
b = 10
mensagem = f'A soma de {a} e {b} é {a + b}.'
print(mensagem)  # Output: A soma de 5 e 10 é 15

# f-strings também permitem formatação de números

pi = 3.14159
mensagem = f'O valor de pi é aproximadamente {pi:.2f}.'
print(mensagem)  # Output: O valor de pi é aproximadamente 3.14

# f-strings também permitem formatação de datas

from datetime import datetime
hoje = datetime.now()
mensagem = f'Hoje é {hoje:%d/%m/%Y}.'
print(mensagem)  # Output: Hoje é 27/04/2024 (ou
# dependendo da data atual)

