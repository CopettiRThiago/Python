# Copiando Listas

# Criando uma lista original
lista_original = [1, 2, 3, 4, 5]

# Copiando a lista usando o método copy()
copia_lista = lista_original.copy()

# Modificando a cópia da lista
copia_lista.append(6)

# Imprimindo ambas as listas para mostrar que são 
# independentes

print("Lista Original:", lista_original)  # Imprime a lista original
print("Cópia da Lista:", copia_lista)  # Imprime a cópia da lista

# Copiando a lista usando slicing
copia_lista_slicing = lista_original[:]  # Cria uma cópia usando slicing

# Modificando a cópia da lista criada com slicing
copia_lista_slicing.append(7)

# Imprimindo ambas as listas para mostrar que são
# independentes

print("Lista Original:", lista_original)  # Imprime a lista original
print("Cópia da Lista (Slicing):", copia_lista_slicing)  # Imprime a cópia da lista criada com slicing

# Copiando a lista usando o construtor list()
copia_lista_construtor = list(lista_original)  # Cria uma cópia usando o construtor list()
print("Cópia da Lista (Construtor):", copia_lista_construtor)  # Imprime a cópia da lista criada com o construtor

