# Precedência de operadores
# A precedência de operadores determina a ordem em 
# que as operações são avaliadas em uma expressão
# A ordem de precedência dos operadores em Python é a seguinte:

# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*), Divisão (/), Módulo (%), Divisão inteira (//)
# 4. Adição (+), Subtração (-)
# 5. Operadores de comparação (==, !=, >, <, >=, <=)
# 6. Operadores lógicos (and, or, not)

# se tem a mesma precedência, é executado da esquerda para a direita

# Exemplo de expressão com diferentes operadores

resultado = 10 + 5 * 2 ** 3
print(resultado)  

# O resultado é 50, pois a exponenciação é avaliada primeiro, 
# depois a multiplicação e por último a adição