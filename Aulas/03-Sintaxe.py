'''
Sintaxe do Python
A sintaxe é a forma como o código deve ser escrito para que o interpretador 
do Python possa entender e executar corretamente.
A sintaxe do Python é baseada em indentação, ou seja, o uso de espaços em branco
para definir blocos de código.

Python é uma linguagem de programação Dinâmica e de tipagem Forte
Dinâmica: o tipo de uma variável é determinado em tempo de execução, ou seja,
não é necessário declarar o tipo da variável antes de usá-la.
Tipagem Forte: o Python não permite operações entre tipos incompatíveis,
como por exemplo, somar uma string com um número.
'''

# Aspas simples
print('Texto')

# Aspas duplas
print("Texto")

# Escape '\' pula o próximo caractere, ou seja, ele é ignorado
print('Texto com aspas simples \' e aspas duplas \'')

# raw string, ou seja, o caractere de escape é tratado como um caractere normal
print(r'Texto com aspas simples \' e aspas duplas \'')

# Inverter a ordem das aspas
print("Texto com aspas simples ' e aspas duplas'")