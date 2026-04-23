# Operador IN e NOT IN
# Os operadores IN e NOT IN são utilizados para verificar se um 
# elemento está presente em uma sequência (como uma string, lista ou tupla).
# in -> está entre
# not in -> não está entre

# Muito utilizado em strings, pois as strings são iteráveis, ou seja, 
# podemos percorrer cada caractere da string.

# Exemplo 1: Usando em strings
texto = "Olá, mundo!"
print('Olá' in texto)     # Saída: True
print('Python' in texto)  # Saída: False

# Exemplo 2: Usando em listas
frutas = ['maçã', 'banana', 'laranja']
print('banana' in frutas)  # Saída: True
print('uva' in frutas)     # Saída: False
print('uva' not in frutas) # Saída: True
