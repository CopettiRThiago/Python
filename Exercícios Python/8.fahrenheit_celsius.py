# Conversor de temperatura. 
# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.

fah = float(input('Informe a temperatura em Fahrenheit : '))

celsius = (fah - 32 ) * 5/9

print(f'{fah:.2f} Fahrenheit equivalem a {celsius:.2f} Celsius ')
