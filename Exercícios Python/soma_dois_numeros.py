# Programa que pede dois números para o usuário
# e mostra a soma entre eles

float_numero_1 = input('Digite o primeiro número : ')
float_numero_2 = input('Digite o segundo número : ')

float_numero_1 = float(float_numero_1)
float_numero_2 = float(float_numero_2)  

soma = float_numero_1 + float_numero_2

print('A soma entre {} e {} é igual a {} '
      .format(float_numero_1, float_numero_2, soma))