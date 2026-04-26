# Faça um programa que peça um valor e mostre na tela 
# se o valor é positivo ou negativo

numero = float(input('Informe um número : '))

if numero > 0:
    print(f'O número {numero} é positivo.')
elif numero < 0 :
    print(f'O número {numero} é negativo')
else: 
    print('Onúmero é zero')