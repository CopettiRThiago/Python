# Lista de Listas

# Criando uma lista de listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos em uma lista de listas
print(matriz[0])  # Imprime a primeira linha da matriz
print(matriz[1][2])  # Imprime o elemento na segunda linha, terceira coluna (6)

# Adicionando uma nova linha à matriz
nova_linha = [10, 11, 12]
matriz.append(nova_linha)  # Adiciona a nova linha à matriz

# Imprimindo a matriz completa
print(matriz)
