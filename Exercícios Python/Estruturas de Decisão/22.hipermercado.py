#### 22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
'''

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos 
de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% 
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''


carne = input('Informe o tipo de carne : \n'
              '[F] Filé Duplo \n'
              '[A] Alcatra \n'
              '[P] Picanha\n\n'
              'Opção desejada : ').upper()

quantidade = float(input('Informe a quantidade desejada em Kg : '))

if carne == 'F':
    tipo = 'Filé Duplo'
    if quantidade > 5:
        total = quantidade * 5.8
    else:
        total = quantidade * 4.9

elif carne == 'A':
    tipo = 'Alcatra'
    if quantidade > 5:
        total = quantidade * 6.8
    else:
        total = quantidade * 5.9

elif carne == 'P':
    tipo = 'Picanha'
    if quantidade > 5:
        total = quantidade * 7.8
    else:
        total = quantidade * 6.9

forma_pagamento = input(
                        'Meios de pagamento : \n\n'
                        '[P] Pix \n'
                        '[C] Cartão de crédito \n'
                        '[D] Débito \n'
                        '[T] Cartão Tabajara (desconto 5%)\n\n'
                        'Informe a opção desejada : '
                        ).upper()

desconto = 0
if forma_pagamento == 'T':
    desconto = total * 0.05
    meio = 'Cartão Tabajara'
elif forma_pagamento == 'P':
    meio = 'Pix'
elif forma_pagamento == 'C':
    meio = 'Cartão de Crédito'
else:
    meio = 'Débito'
print()
print(f'{'  NOTA FISCAL  ':-^40}')
print()
print(f'Tipo de produto : {tipo}')
print(f'Quantidade : {quantidade:.2f} Kg')
print(f'Valor total : R$ {total:.2f}')
print(f'Forma de pagamento : {meio}')
print(f'Desconto : R$ {desconto}')
print(f'Valor a pagar : R$ {total - desconto:.2f}')


# Simplificada

# tipo = input('Informe o tipo da carne: ')
# quantidade = float(input('Informe a quantidade de carne: '))
# pagamento = input('Escolha a forma de pagamento (C - Cartão Tabajara/D - Dinheiro): ')

# if tipo == 'File Duplo' and quantidade > 5:
#     total = 5.8 * quantidade
# elif tipo == 'File Duplo' and quantidade <= 5:
#     total = 4.9 * quantidade
# elif tipo == 'Alcatra' and quantidade > 5:
#     total = 6.8 * quantidade
# elif tipo == 'Alcatra' and quantidade <= 5:
#     total = 5.9 * quantidade
# elif tipo == 'Picanha' and quantidade > 5:
#     total = 7.8 * quantidade
# elif tipo == 'Picanha' and quantidade <= 5:
#     total = 6.9 * quantidade
    
# print('--- CUPOM FISCAL ---')
# print('Tipo da carne:', tipo)
# print('Quantidade:', quantidade, 'kg')
# print('Preço total: R$', total)
# print('Forma de pagamento:', pagamento)

# desconto = 0.05 * total if pagamento == 'C' else 0

# print('Desconto: R$', desconto)
# print('Valor a pagar: R$', total - desconto)

