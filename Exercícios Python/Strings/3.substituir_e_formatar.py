# Substitua todas as ocorrências de uma palavra por outra 
# e retorne a frase com a primeira letra de cada sentença em maiúscula.

frase = input('Informe a frase : ')
palavra_antiga = input('Informe a palavra a ser substituída : ')
palavra_nova = input('Informe a nova palavra : ')

# Substituir a palavra antiga pela nova

nova_frase = frase.replace(palavra_antiga, palavra_nova)

# Colocar a primeira letra de cada sentença em maiúscula
nova_frase_formatada = nova_frase.title()

print('Frase original : ', frase)
print('Frase modificada : ', nova_frase_formatada)
