
num = int(input('enter a number: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)


print('Escolha uma das bases: ')
print('1- Binario')
print('2- Octal')
print('3- Hexadecimal')
opcao = int(input('Informe uma das Opções: '))
if(opcao == 1 ):
    print(f'O numero em Binario é {binario}')
elif(opcao == 2):
    print(f'O numero em octal é {octal}')
elif(opcao == 3):
    print(f'O numero hexadecimal é {hexadecimal}')
else:
    print('Opcao invalida')
