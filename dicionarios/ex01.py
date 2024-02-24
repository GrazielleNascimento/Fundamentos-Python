emails_gerentes = {
    "Iguatemi": "Iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com",
}

precos_produtos = {"lampada": 100, "mesa": 500, "laptop": 6000,  }

#a chave é a posicao do elemento
#descobrir o meail do shopping iguatemi
email = emails_gerentes['Iguatemi']
print(email)

#adicionar um shopping novo
emails_gerentes["Super Shopping"] = "supershopping@gmail.com"
print(emails_gerentes)

#descobrir todos os shoppings que tenho

print('\nUsando o for para as chaves\n')
for shopping in emails_gerentes: #para cada shopping no email_gerentes, foi nomeada que os elementos sao shoppings
    print(shopping)

print('\nUsando o Keys para as chaves\n')
print(emails_gerentes.keys())

print('\nUsando o for para os valores\n')
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)
 
print('\nUsando o values para os valores\n')
print(emails_gerentes.values())


print('Retirar um item')
emails_gerentes.pop('Barra')
print(emails_gerentes)


print('Veriificar se existe no dicionario')
if 'Barra' in emails_gerentes: 
    print('existe') 
else:
    print('Não existe')
