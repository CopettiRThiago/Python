# Programa que pede uma string para o usuário e retorna
# a quantidade de vogais separadamente

texto = input('Informe o texto : ').lower()

vogal_a = vogal_e = vogal_i = vogal_o = vogal_u = 0

for caractere in texto:
    if caractere == 'a':
        vogal_a += 1
    elif caractere == 'e':
        vogal_e += 1
    elif caractere == 'i':
        vogal_i += 1
    elif caractere == 'o':
        vogal_o += 1
    elif caractere == 'u':
        vogal_u += 1

print('Contagem de vogais : \n')
print(f'Vogal A : {vogal_a}')
print(f'Vogal E : {vogal_e}')
print(f'Vogal I : {vogal_i}')
print(f'Vogal O : {vogal_o}')
print(f'Vogal U : {vogal_u}')