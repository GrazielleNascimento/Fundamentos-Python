print('{:*^50}'.format('The Multiplication Table'))
number = int(input('Enter the number for the Multiplication table: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(number, i, number * i))

# O :2 dentro das chaves {} especifica um formato para o valor que será colocado ali: diz para o Python reservar no mínimo 2 espaços de caracteres para aquele valor. Isso é útil para alinhamento, especialmente quando você quer que os seus dados apareçam alinhados em colunas.
print('*' * 50)
