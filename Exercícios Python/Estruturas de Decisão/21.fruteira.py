#### 21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
'''
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
 receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a 
 quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva 
 o valor a ser pago pelo cliente.
'''

qtde_morango = float(input('Informe a quantidade de morango em Kg: '))
qtde_maca = float(input('Informe a quantidade de maçãs em Kg: '))

peso_total = qtde_morango + qtde_maca

if qtde_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

valor_morango = qtde_morango * preco_morango

if qtde_maca <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

valor_maca = qtde_maca * preco_maca

valor_total = valor_maca + valor_morango

if peso_total > 8 or valor_total > 25:
    valor_final = valor_total * 0.9
else:
    valor_final = valor_total

print('Valor Final : ')
print(f'{qtde_morango} kg de morango : R$ {valor_morango:.2f}')
print(f'{qtde_maca} kg de maçã : R$ {valor_maca:.2f}')
print(f'Valor total : R$ {valor_total:.2f}')
print(f'Desconto : R$ {valor_total - valor_final:.2f}')
print(f'Valor a pagar : R$ {valor_final:.2f}')

# Simplificada

qtd_morango = float(input('Informe a quantidade de morango: '))
qtd_maca = float(input('Informe a quantidade de maçã: '))

if qtd_morango > 5:
    total_morango = 2.2 * qtd_morango
else:
    total_morango = 2.5 * qtd_morango
    
if qtd_maca > 5:
    total_maca = 1.5 * qtd_maca
else:
    total_maca = 1.8 * qtd_maca
    
if qtd_morango + qtd_maca > 8 or total_morango + total_maca > 25:
    total = (total_morango + total_maca) * 0.9
else:
    total = total_morango + total_maca
    
print('Total a pagar: R$', total)
