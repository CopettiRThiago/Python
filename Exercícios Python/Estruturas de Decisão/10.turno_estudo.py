# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a 
# mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

nome = input('Nome : ')
print(
    'Informe o período em que estuda: \n'
    '[M] Matutino \n'
    '[V] Vespertino \n'
    '[N] Noturno \n'
    )
periodo = input('Qual sua opção ? ').strip().upper()

if periodo == 'M':
    print(f'Bom dia {nome}, bons estudos')
elif periodo == 'V':
    print(f'Boa tarde {nome}, bons estudos')
elif periodo == 'N':
    print(f'Boa noite {nome}, bons estudos')
else:
    print('Valor inválido')