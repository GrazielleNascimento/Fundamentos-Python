import random 
from time import sleep

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)

numero = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')

sleep(3)

sorteado = random.randint(0,5)

if(numero == sorteado):
    print(f'Parabens voce acertou o numero{sorteado}')
else:
    print(f'Voce errou, o numero era o {sorteado}')


