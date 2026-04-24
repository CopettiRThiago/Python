# Programa que recebe a largura e o comprimento
# de um apartamento e calcula a área em metros quadrados

largura = float(input('Informe a largura do aparatemento em metros : '))
comprimento = float(input('Informe o comprimento do apartamento em metros : '))

area = largura * comprimento
print(
    f'Um apartamento de {largura} metros de largura e \n'
    f'{comprimento} metros de comprimento  \n'
    f'tem uma área de {area:.2f} m²'
    )

