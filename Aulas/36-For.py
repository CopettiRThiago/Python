# For

# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário,
#  conjunto ou string) ou outros objetos iteráveis. Ele executa um bloco de código para 
# cada item na sequência.

# O loop For é útil quando você sabe o número de iterações ou quando deseja iterar sobre 
# uma coleção de itens. 

# A sintaxe básica do loop for é a seguinte:

# for item in iterável:
    # Faça algo com o item
    # print(item)

print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

print('For em uma string')
string = "Python"
for caractere in string:
    print(caractere)

# break e continue

# O comando break é usado para sair imediatamente do loop, enquanto o comando 
# continue é usado para pular a iteração atual e continuar com a próxima.

print("Exemplo de break")
for i in range(10):
    if i == 5:
        break  # Sai do loop quando i é igual a 5
    print(i)

print("Exemplo de continue")
for i in range(10):
    if i % 2 == 0:
        continue  # Pula a iteração atual se i for par
    print(i)

