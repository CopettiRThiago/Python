# Verificar se a palavra ou frase é um 
# palíndromo ( igual de trás para frente)

texto = input('Informe a palavra ou frase : ').strip().upper()
texto = texto.split()
texto_ajustado = ''.join(texto)

inverso = texto_ajustado[::-1]

if texto_ajustado == inverso:
    print(f'{texto_ajustado} é um palíndromo')
    print(f'{inverso} é o inverso')
else:
    print(f'{texto_ajustado} não é um palíndromo')
    print(f'{inverso} ')