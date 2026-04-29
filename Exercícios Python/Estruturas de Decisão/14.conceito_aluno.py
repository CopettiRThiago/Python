# Faça um programa que lê as duas notas parciais obtidas por um 
# aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# Em seguida, mostre qual conceito o aluno teve. 

nota_1 = float(input('Informe a primeira nota : '))
nota_2 = float(input('Informe a segunda nota : '))

media = (nota_1 + nota_2) / 2

if 9 < media <= 10:
    conceito = 'A'
elif 7.5 < media <= 9:
    conceito = 'B'
elif 6 < media <= 7.5:
    conceito = 'C'
elif 4 < media <= 6:
    conceito = 'D'
elif 0 <= media <= 4:
    conceito = 'E'
else:
    print('Informação de notas não correspondem')

print(f'Com as notas {nota_1} e {nota_2} a media foi {media:.2f} e o conceito foi {conceito}')