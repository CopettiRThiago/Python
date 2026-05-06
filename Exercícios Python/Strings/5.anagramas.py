# Verifique se duas palavras são anagramas uma da outra.

def clean(s):
    return ''.join(ch.lower() for ch in s if ch.isalnum())

s1 = input('Digite a primeira frase: ')
s2 = input('Digite a segunda frase: ')

c1 = clean(s1)
c2 = clean(s2)

if sorted(c1) == sorted(c2):
    print('São anagramas')
else:
    print('Não são anagramas')

