# Programa que recebe o valor da hora trabalhada
# e o número de horas trabalhadas no mÊs
# calcula o salário mensal do funcionário

valor_hora = float(input('Valor da hora trabalhada : R$ '))
horas_trabalhadas = float(input('Número de horas trabalhadas no mês : '))

salario_mensal = valor_hora * horas_trabalhadas

print(f'Horas trabalhadas : {horas_trabalhadas} horas')
print(f'Valor da hora trabalhada : R$ {valor_hora:.2f}')
print(f'Salário mensal : R$ {salario_mensal:.2f}')