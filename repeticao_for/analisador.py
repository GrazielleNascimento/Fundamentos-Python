somaidade = 0
mediaidade = 0
maioridadehomem= 0
nomevelho = ''
for p in range(1, 5):
    print(f'---- {p} Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    somaidade = somaidade + idade
    
    if p == 1 and sexo in "Mn":
        maioridadehomem = idade
        nomevelho = nome

    if sexo in "Mn" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    
    mediaidade = somaidade / 4

print(f'A media de idade do grupo é de {mediaidade} ')
print(f'O Homem mais velho tem {idade} anos e se chama {nome}')

    
