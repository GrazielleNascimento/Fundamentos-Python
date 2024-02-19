# This program reads the amount of money a person has in Brazilian Reais (R$)
# and calculates how many US dollars (USD) they can purchase based on the current exchange rate.

print('{:*^50}'.format('Currency Exchange Program'))
reais = float(input('\nHow much money do you have in reais? '))
dollars_can_buy = reais / 3.27

print(f'With {reais} reais, you can buy {dollars_can_buy:.2f} dollars.')
