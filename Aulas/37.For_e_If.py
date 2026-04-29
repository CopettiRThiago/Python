# For e If
# O loop for e a estrutura condicional if são frequentemente usados juntos 
# para iterar sobre uma sequência e executar ações com base em condições específicas.

# estrutura básica do for com if:

# for item in iterável:
#     if condição:
#         Faça algo com o item

# Exemplo 1: Imprimir apenas os números pares de uma lista
print("Números pares em uma lista")
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

