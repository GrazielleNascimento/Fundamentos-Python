from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento  
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2024 ')

if(idade == 18):
    print(f'Voce tem que se alistar IMEDIATAMENTE!')
elif(idade < 18):
    saldo =  18 - idade
    print(f'Voce ainda nao tem 18 anos. Ainda faltam {saldo} anos para o alistamento')
    ano = ano_atual + saldo
    print(f'Seu alistamento sera em {ano}')
elif(idade > 18):
     saldo = idade - 18
     print(f'Voce ja deveria ter se alistado ha {saldo} anos')
     ano = ano_atual - saldo
     print(f'Seu alistamento foi em {ano}')
