#### 4. Faça um Programa que verifique se o e-mail 
# digitado faz parte dos e-mails de spam.

email_spam = 'fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com'

email = input('Informe o e-mail para verificação de spam : ')

if email in email_spam:
    print(f'O e-mail {email} é spam')
else:
    print(f'O e-mail {email} não é spam')