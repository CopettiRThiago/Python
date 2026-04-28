#### 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('Informe o primeiro número : '))
numero_2 = float(input('Informe o segundo número : '))
numero_3 = float(input('Informe o terceiro número : '))

if numero_1 > numero_2 and numero_1 > numero_3:
    if numero_2 > numero_3:
        print(f'Ordem decrescente : {numero_1} {numero_2} {numero_3}')
    else:
        print(f'Ordem decrescente : {numero_1} {numero_3} {numero_2}')

if numero_2 > numero_1 and numero_2 > numero_3:
    if numero_1 > numero_3:
        print(f'Ordem decrescente : {numero_2} {numero_1} {numero_3}')
    else:
        print(f'Ordem decrescente : {numero_2} {numero_3} {numero_1}')

if numero_3 > numero_1 and numero_3 > numero_2:
    if numero_2 > numero_1:
        print(f'Ordem decrescente : {numero_3} {numero_2} {numero_1}')
    else:
        print(f'Ordem decrescente : {numero_3} {numero_1} {numero_2}')