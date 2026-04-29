#### 15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH.
#  Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, 
# para montar o calendário de forma correta. Faça um Programa que peça um número correspondente 
# a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Informe o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
