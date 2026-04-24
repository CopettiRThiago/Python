# Program que pede a nota de 4 provas, 
# calcula a média e diz se o aluno foi aprovado ou reprovado

nota_1 = float(input('Informe a primeira nota : '))
nota_2 = float(input('Informe a segunda nota : '))
nota_3 = float(input('Informe a terceira nota : '))
nota_4 = float(input('Informe a quarta nota : '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média final do aluno foi {media:.2f}')