# Dada uma string com números misturados (ex: "tem 3 maças e 12 laranjas"),
# extraia todos os inteiros e retorne a soma.

texto = input('Informe o texto com números : ')
numeros_extraidos = []
for caractere in texto:
    if caractere.isdigit():
        numeros_extraidos.append(int(caractere))
soma = sum(numeros_extraidos)

print(f'Os números extraídos são: {numeros_extraidos}')
print(f'A soma dos números extraídos é: {soma}')
