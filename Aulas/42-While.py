# While

# O loop é uma estrutura de repetição que executa um bloco de código 
# enquanto uma condição for verdadeira.

# Estrutura do while:
# while condição:
#     bloco de código

# Exemplo 1: Contagem de 1 a 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Incrementa o contador para evitar loop infinito

# Exemplo 2: Verificação de senha
senha_correta = "python123"
senha_usuario = ""

while senha_usuario != senha_correta:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == senha_correta:
        print("Acesso concedido!")
    else:
        print("Senha incorreta. Tente novamente.")

# Exemplo 3: Soma de números até o usuário decidir parar
soma = 0
while True:
    numero = input("Digite um número para somar (ou 'sair' para terminar): ")
    if numero.lower() == 'sair':
        break  # Sai do loop
    elif numero.isdigit():
        soma += int(numero)
    else:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")