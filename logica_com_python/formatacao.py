n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
di = n1 / n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisao é {:.3f}'.format(s, m, di), end = ' ')
print('Divisao inteira {} e potencia {}'. format(di, e))
