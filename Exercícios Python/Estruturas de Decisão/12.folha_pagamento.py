#### 12 . Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
# (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde 
# ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor 
# da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:<br>
# Salário Bruto até 900 (inclusive) - isento<br>
# Salário Bruto até 1500 (inclusive) - desconto de 5%<br>
# Salário Bruto até 2500 (inclusive) - desconto de 10%<br>
# Salário Bruto acima de 2500 - desconto de 20%<br>
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R\\$ 1100,00<br>
# (-) IR (5%)                     : R\\$   55,00<br>
# (-) INSS ( 10%)                 : R\\$  110,00<br>
# FGTS (11%)                      : R\\$  121,00<br>
# Total de descontos              : R\\$  165,00<br>
# Salário Liquido                 : R\\$  935,00<br>

###### Obs: Não vamos nos preocupar tanto com a 
# formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)

valor_hora = float(input('Valor da hora trabalhada : R$ '))
total_horas = float(input('Horas trabalhadas : '))

salario_bruto = valor_hora * total_horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 0.05
elif salario_bruto <= 2500:
    ir = 0.1
elif salario_bruto > 2500:
    ir = 0.2

desconto_ir = salario_bruto * ir
desconto_inss = salario_bruto * 0.10
desconto_fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print()
print(f'{'Folha de Pagamento :':^40}\n')

print(f'Salário Bruto ( {valor_hora:.0f} * {total_horas:.0f}) {'R$ ':.>15}{salario_bruto:.2f}')
print(f'{'(-) IR ('}{ir*100:.0f}{'%)':<}     {'R$ ':.>24}{desconto_ir:.2f}')
print(f'{'(-) INSS ( 10 % )'}............ {'R$ ':.>10}{desconto_inss:.2f}')
print(f'{'FGTS ( 11% )'}................. {'R$ ':.>10}{desconto_fgts:.2f}')
print(f'Total de descontos ................. R$  {total_descontos:.>.2f}')
print(f'Salário Líquido .................... R$ {salario_liquido:.2f}')
