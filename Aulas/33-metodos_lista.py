# Métodos de Lista

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Adicionando um elemento ao final da lista
lista.append(6)

# Inserindo um elemento em uma posição específica
lista.insert(2, 10)  # Insere o número 10 na posição

# Removendo um elemento pelo valor
lista.remove(3)  # Remove o número 3 da lista

# Removendo um elemento pelo índice
del lista[0]  # Remove o primeiro elemento da lista

# Contando o número de ocorrências de um elemento
count_10 = lista.count(10)  # Conta quantas vezes o número 10 aparece na lista

# Ordenando a lista
lista.sort()  # Ordena a lista em ordem crescente

# Invertendo a ordem da lista
lista.reverse()  # Inverte a ordem dos elementos na lista

# Imprimindo a lista final
print(lista)

# limpando a lista
lista.clear()  # Remove todos os elementos da lista

# Copiando a lista

nova_lista = lista.copy()  # Cria uma cópia da lista
print(nova_lista)  # Imprime a nova lista (que está vazia)

