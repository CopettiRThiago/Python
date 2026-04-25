# Conversor de moedas

valor = float(input('Quanto dinheiro você tem na carteira? '))

dolar = valor/5.33

print('\nCom R${:.2f} você pode comprar US${:.2f}'.format(valor, dolar))