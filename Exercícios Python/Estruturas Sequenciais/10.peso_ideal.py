# Tendo como dados de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# 72.7 * h - 58

altura = float(input('Informe sua altura em metros : '))

peso_ideal = 72.7 * altura -58

print(f'Com {altura} m de altura, o peso ideal é {peso_ideal:.2f}')