# print(f'**🌟 Big Sale Promotion! 🌟**')

text = 'Big Sale Promotion!'
width = 35

# Usando o método .center() com o emoji desejado como preenchimento
result = text.center(width, '🌟')
print(result)

value= float(input('\nEnter the value of product: '))
discount_rate = 0.05
new_value = value - (value * discount_rate)

print(f'The new value of the product is {new_value:.2f}')
