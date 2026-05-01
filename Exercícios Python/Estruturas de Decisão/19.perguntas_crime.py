# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# Telefonou para a vítima ?
# Esteve no local do crime ?
# Mora perto da vítima ? 
# Devia para a vítima ?
# Já trabalhou com a vítima ?

resposta = input('Telefonou para a vítima?')

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

if resposta == 'sim':
    p1 = 1
    
resposta = input('Esteve no local do crime?')

if resposta == 'sim':
    p2 = 1
    
resposta = input('Mora perto da vítima?')

if resposta == 'sim':
    p3 = 1
    
resposta = input('Devia para a vítima?')

if resposta == 'sim':
    p4 = 1
    
resposta = input('Já trabalhou com a vítima?')

if resposta == 'sim':
    p5 = 1

total = p1 + p2 + p3 + p4 + p5

if total == 2:
    print('Suspeita')
elif 3 <= total <= 4:
    print('Cúmplice')
elif total == 5:
    print('Assassino')
else:
    print('Inocente')
