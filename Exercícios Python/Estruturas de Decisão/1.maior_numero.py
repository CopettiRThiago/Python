# Faça um programa que peça dois números e mostre o maior deles

numero_1 = float(input('Informe o primeiro número :'))
numero_2 = float(input('Informe o segundo número : '))

if numero_1 > numero_2:
    print(f'O número {numero_1} é maior que o número {numero_2}.')
elif numero_2 > numero_1:
    print(f'O número {numero_2} é maior que o número {numero_1}.')
else:
    print(f'O número digitados são iguais')
    