# Faça um Programa que pergunte quanto você 
# ganha por hora e o número de horas trabalhadas no mês.
# Calcule o salário bruto (horas * salario por hora)
# Calcule o desconto do IR (11% do salário bruto)
# Calcule o desconto do INSS (8% do salário bruto)
# Calcule o desconto do sindicato (5% do salário bruto)
# Calcule o salário líquido (salário bruto - descontos)

valor_hora = float(input('Valor da hora : '))
horas_trabalhadas = float(input('Horas trabalhadas : '))

salario_bruto = valor_hora * horas_trabalhadas

ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salário bruto : R$ {salario_bruto:.2f}')
print(f'Imposto de renda : R$ {ir:.2f}')
print(f'INSS : R$ {inss:.2f}')
print(f'Sindicato : R$ {sindicato}')
print(f'Salário final : R$ {salario_liquido:.2f}')
