# Iterando strings com while

nome = input('Qual seu nome ? ').strip().title()
string = input('Que separador você quer utilizar ? ')
indice = 0
nova_string = ''

while indice < len(nome):
    nova_string += string + nome[indice]
    indice+= 1
    
nova_string += string   # apenas para colocar a string no final
print(nova_string)