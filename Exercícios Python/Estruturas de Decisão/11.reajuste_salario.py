#### 11. As Organizações Tabajara resolveram dar um aumento de salário 
# aos seus colaboradores e lhe contraram para desenvolver o programa que 
# calculará os reajustes. Faça um programa que recebe o salário de um 
# colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:


salario = float(input('Informe o salário em R$: '))

if salario <= 280:
    percentual = 0.2    
elif salario <= 700:
    percentual = 0.15
elif salario <= 1500:
    percentual = 0.1
else:
    percentual = 0.05

novo_salario = salario * (1 + percentual)
aumento = novo_salario - salario

print(f'Salário antes do reajuste: R$ {salario:.2f}')
print(f'Percentual de aumento: {percentual * 100}%')
print(f'O aumento foi de R$ {aumento:.2f}')
print(f'Salário após aumento: R$ {novo_salario:.2f}')


    