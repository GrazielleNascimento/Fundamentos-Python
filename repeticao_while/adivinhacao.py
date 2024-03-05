
import random 

pc = random.randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi??')
acertou = False
palpites = 0
while not acertou:
    vc = int(input('Adivinhe o numero: '))
    palpites += 1

    if vc == pc:
         acertou = True
    else:
        if vc < pc:
           print('Mais...')
        elif vc > pc:
            print('Menos..')

print(f'Acertoou! foram {palpites} palpites')

