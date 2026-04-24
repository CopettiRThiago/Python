# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.

celsius = float(input('Informe a temperatura em Celsius : '))

fah = (celsius * 9/5) + 32

print(f'{celsius:.2f} Celsius equivalem a {fah:.2f} Fahreinheit ')

