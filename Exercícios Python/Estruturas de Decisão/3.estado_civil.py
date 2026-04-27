#### 3. Faça um Programa que verifique o estado civil de uma pessoa. 
# Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), 
# "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário 
# seu programa deve escrever o estado civil:

nome = input('Informe seu nome : ')
estado_civil = input(
                    'Estado civil \n'
                     'C = Casado \n'
                     'S = Solteiro \n'
                     'D = Divorciado \n'
                     'V = Viúvo \n'
                     'O = Outros\n'
                     'Informe seu estado civil : '
                     ).strip().upper()

if estado_civil == 'C':
    print(f'Seu nome é {nome} e seu estado civil é Casado(a)')
elif estado_civil == 'S':
    print(f'Seu nome é {nome} e seu estado civil é Solteiro(a)')
elif estado_civil == 'D':
    print(f'Seu nome é {nome} e seu estado civil é Divorciado(a)')
elif estado_civil == 'V':
    print(f'Seu nome é {nome} e seu estado civil é Viúvo(a)')
else:
    print(f'Seu nome é {nome} e você optou por não informar seu estado civil')




