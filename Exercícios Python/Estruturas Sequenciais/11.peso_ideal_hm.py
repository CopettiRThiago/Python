#### 11. Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: $P = 72,7h - 58$
# Para mulheres: $P = 62,1h - 44,7$

altura = float(input('Informe a altura em metros : '))

peso_ideal_homem = 72.7 * altura - 58
peso_ideal_mulher = 62.1 * altura - 44.7

print(
      f'Com {altura:.2f}m de altura, o pesoa ideal \n'
      f'para mulheres é de {peso_ideal_mulher:.2f} kg \n'
      f'e para homens é de {peso_ideal_homem:.2f} kg'
      )