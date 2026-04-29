#### 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

dia = int(input('Informe o número : '))

if dia == 1:
    dia_semana = 'Domingo'
elif dia == 2:
    dia_semana = 'Segunda Feira'
elif dia == 3:
    dia_semana = 'Terça Feira'
elif dia == 4:
    dia_semana = 'Quarta Feira'
elif dia == 5:
    dia_semana = 'Quinta Feira'
elif dia == 6:
    dia_semana = 'Sexta Feira'
elif dia == 7 :
    dia_semana = 'Sábado'
else:
    print(f'O dia {dia} digitado não correponde a nenhum dia da semana.')

print(f'Você digitou o número {dia} que corresponde a {dia_semana} ')