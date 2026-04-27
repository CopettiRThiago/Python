#### 6. Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.

orcamento_1 = float(input('Informe o primeiro orçamento : '))
orcamento_2 = float(input('Informe o segundo orçamento : '))
orcamento_3 = float(input('Informe o terceiro orçamento : '))

if orcamento_1 > orcamento_2 and orcamento_1 > orcamento_3:
    print(f'Maior orçamento : {orcamento_1:.2f}')
elif orcamento_2 > orcamento_1 and orcamento_2 > orcamento_3:
    print(f'Maior orçamento : {orcamento_2:.2f}')
elif orcamento_3 > orcamento_1 and orcamento_3 > orcamento_2:
    print(f'Maior orçamento : {orcamento_3:.2f}')

    
