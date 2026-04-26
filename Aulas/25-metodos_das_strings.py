# Métodos das strings
'''
    São funções que já estão implementadas para serem usadas com as strings
    Para usar um método, basta chamar a string seguida de um ponto e o nome do método
    Esrtutura: string.metodo()
    Alguns métodos podem receber argumentos, outros não
    Os métodos retornam um valor, que pode ser uma nova string ou um valor booleano

    upper() - transforma a string em maiúscula
    lower() - transforma a string em minúscula
    title() - transforma a primeira letra de cada palavra em maiúscula
    strip() - remove os espaços em branco no início e no final da string
    replace() - substitui uma parte da string por outra
    split() - divide a string em uma lista de palavras
    spliltlines() - divide a string em uma lista de linhas
    join() - junta uma lista de palavras em uma string
    find() - encontra a posição de uma substring na string
    count() - conta quantas vezes uma substring aparece na string
    startswith() - verifica se a string começa com uma substring
    endswith() - verifica se a string termina com uma substring
    isalpha() - verifica se a string contém apenas letras
    isdigit() - verifica se a string contém apenas números
    isspace() - verifica se a string contém apenas espaços em branco
    len() - retorna o comprimento da string
    format() - formata a string com valores
    f-string - formata a string com valores usando a sintaxe f"{}"
    capitalize() - transforma a primeira letra da string em maiúscula
    swapcase() - inverte as letras maiúsculas e minúsculas da string
    zfill() - preenche a string com zeros à esquerda
    lstrip() - remove os espaços em branco no início da string
    rstrip() - remove os espaços em branco no final da string
    center() - centraliza a string em um campo de largura especificada
    ljust() - alinha a string à esquerda em um campo de largura especificada
    rjust() - alinha a string à direita em um campo de largura especificada
    zfill() - preenche a string com zeros à esquerda
    islower() - verifica se a string contém apenas letras minúsculas
    isupper() - verifica se a string contém apenas letras maiúsculas
    isalnum() - verifica se a string contém apenas letras e números
    isdecimal() - verifica se a string contém apenas números decimais
    isidentifier() - verifica se a string é um identificador válido
    isprintable() - verifica se a string contém apenas caracteres imprimíveis
    casefold() - transforma a string em minúscula, mas de forma mais agressiva que lower()
    isnumeric() - verifica se a string contém apenas números
'''

# Exemplo de uso dos métodos das strings
texto = "   Olá, Mundo!   "
print(texto.upper()) # "   OLÁ, MUNDO!   "
print(texto.lower()) # "   olá, mundo!   "
print(texto.title()) # "   Olá, Mundo!   "
print(texto.strip()) # "Olá, Mundo!"
print(texto.replace("Mundo", "Python")) # "   Olá, Python!   "
print(texto.split()) # ['Olá,', 'Mundo!']
print(texto.splitlines()) # ['   Olá, Mundo!   ']
print("-".join(texto.split())) # "Olá,-Mundo!"
print(texto.find("Mundo")) # 8
print(texto.count("o")) # 2
print(texto.startswith("   Olá")) # True
print(texto.endswith("Mundo!   ")) # True
print(texto.isalpha()) # False
print(texto.isdigit()) # False
print(texto.isspace()) # False
print(len(texto)) # 18
print("Olá, {}!".format("Python")) # "Olá, Python!"
print(f"Olá, {'Python'}!") # "Olá, Python!"
print(texto.capitalize()) # "   olá, mundo!   "
print(texto.swapcase()) # "   oLÁ, mUNDO!   "
print(texto.zfill(20)) # "000000   Olá, Mundo!   "
print(texto.lstrip()) # "Olá, Mundo!   "
print(texto.rstrip()) # "   Olá, Mundo!"
print(texto.center(30)) # "       Olá, Mundo!       "
print(texto.ljust(30)) # "   Olá, Mundo!               "
print(texto.rjust(30)) # "               Olá, Mundo!   "
print(texto.islower()) # False
print(texto.isupper()) # False
print(texto.isalnum()) # False
print(texto.isdecimal()) # False
print(texto.isidentifier()) # False
print(texto.isprintable()) # True
print(texto.casefold()) # "   olá, mundo!   "
print(texto.isnumeric()) # False
