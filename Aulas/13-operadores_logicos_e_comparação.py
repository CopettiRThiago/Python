# Operadores lógicos e de comparação

# Os operadores de comparação são usados para comparar valores
# Os principais operadores de comparação em Python são:
'''
    Operadores de comparação (relacionais)
OP        Significado        Exemplo (True)
>         maior               2 > 1
>=        maior ou igual      2 >= 2
<         menor               1 < 2
<=        menor ou igual      2 <= 2
==        igual               'a' == 'a'
!=        diferente           'a' != 'b'
'''

# Operadores lógicos
# Os operadores lógicos são usados para combinar 
# expressões booleanas
# Os principais operadores lógicos em Python são:
# and (e) - retorna True se ambas as expressões forem verdadeiras
# or (ou) - retorna True se pelo menos uma das expressões for verdadeira

# Exemplo de operadores lógicos
a = 10
b = 5
c = 15
if a > b and c > a:
    print('Ambas as condições são verdadeiras!')
if a > b or c < a:
    print('Pelo menos uma das condições é verdadeira!')

