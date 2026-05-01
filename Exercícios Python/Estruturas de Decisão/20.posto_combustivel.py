# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

combustivel = input('Digite [A] para álcool ou [G] para gasolina : ').upper()
litros = float(input('Litros abastecidos : '))

if combustivel == 'A':
    preco = 1.9
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif combustivel == 'G':
    preco = 2.5
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

valor_total = litros * preco
desconto_total = valor_total * desconto
valor_final = valor_total - desconto_total

print(f'{'  Nota Fiscal  ':-^40}')
print(f'Quantidade abastecida : {litros} litros')
print(f'Tipo de combustível : {combustivel}')
print(f'Valor total : R$ {valor_total:.2f}')
print(f'Desconto total : R$ {desconto_total:.2f}')
print(f'Valor a pagar : R$ {valor_final:.2f}')

# Resolução simplificada

# tipo = input('Informe o tipo de combustível: ')
# quantidade = float(input('Informe a quantidade de combustível: '))

# if tipo == 'A' and quantidade <= 20:
#     total = (1.9 * quantidade) * 0.97
# elif tipo == 'A' and quantidade > 20:
#     total = (1.9 * quantidade) * 0.95
# elif tipo == 'G' and quantidade <= 20:
#     total = (2.5 * quantidade) * 0.96
# elif tipo == 'G' and quantidade > 20:
#     total = (2.5 * quantidade) * 0.94

# print('Total a pagar: R$', total)