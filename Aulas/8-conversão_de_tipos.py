# Conversão de Tipos
# Em Python, é possível converter um tipo de dado para outro usando funções de conversão.
# As principais funções de conversão são:

# int(): converte um valor para inteiro
# float(): converte um valor para float (número decimal)
# str(): converte um valor para string (texto)

# Exemplos de conversão de tipos:
# Convertendo uma string para inteiro
numero_str = "123"
numero_int = int(numero_str)
print(numero_int)  # Output: 123
print(type(numero_int))  # Output: <class 'int'>

# Convertendo um número inteiro para float
numero_int = 456
numero_float = float(numero_int)
print(numero_float)  # Output: 456.0
print(type(numero_float))  # Output: <class 'float'>

# Convertendo um número para string
numero = 789
numero_str = str(numero)
print(numero_str)  # Output: "789"
print(type(numero_str))  # Output: <class 'str'>
# Atenção:

# string vazio é False e string com conteúdo é True
