# Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e presentar:

nota_1 = float(input('Informe a primeira nota : '))
nota_2 = float(input('Informe a segunda nota : '))
nota_3 = float(input('Informe a terceira nota : '))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(f'Aluno Aprovado, média final {media:.2f}')
elif media < 7:
    print(f'Aluno Reprovado, média final {media:.2f}')
elif media == 10:
    print(f'Aluno Aprovado com distinção com média {media:.2f}')