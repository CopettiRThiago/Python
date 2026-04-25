# Aluguel de carros

# Programa recebe a quantidade de dias e km rodados, calcula o 
# valor a pagar sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

dia = int(input('Quantos dias alugados ? '))
km_rodados = float(input('Quantos km rodados ? '))

diaria_total = dia * 60
km_total = km_rodados * 0.15

valor_total = diaria_total + km_total

print('O total a pagar é de R$ {:.2f}'.format(valor_total))
print('Foram rodados {} kilometros totalizando R$ {:.2f}'.format(km_rodados,km_total))
print('O carro foi alugado por {} dias e o valor foi de {:.2f}'.format(dia, diaria_total))


# fórmula mais simples

# valor_total = (dia * 60) + (km_rodados * 0.15)

