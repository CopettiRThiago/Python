# Adicionando e Removendo Elementos de uma Lista em Python

# Criando uma lista de carros
carros = ["Fiat", "Ford", "Chevrolet"]

# Adicionando um elemento ao final da lista
# lista.append('item')

carros.append("Volkswagen")
print(carros)  # Output: ['Fiat', 'Ford', 'Chevrolet', 'Volkswagen']

# Adicionando um elemento em uma posição específica
# lista.insert(índice, 'item')

carros.insert(1, "BMW")
print(carros)  # Output: ['Fiat', 'BMW', 'Ford', 'Chevrolet', 'Volkswagen']

# Removendo um elemento da lista
# lista.remove('item')
carros.remove("Ford")
print(carros)  # Output: ['Fiat', 'BMW', 'Chevrolet', 'Volkswagen']

# Removendo um elemento por índice
# lista.pop(índice)

carros.pop(2)
print(carros)  # Output: ['Fiat', 'BMW', 'Volkswagen']

# diferente de remove(), pop() retorna o elemento removido
carro_removido = carros.pop(0)
print(f"Carro removido: {carro_removido}")  # Output: Carro removido: Fiat
print(carros)  # Output: ['BMW', 'Volkswagen']

# Limpando a lista
# lista.clear()

carros.clear()
print(carros)  # Output: []

