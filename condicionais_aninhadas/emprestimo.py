house_value = float(input('Enter the house value: '))
salary = float(input('Enter your salary: '))
years_to_pay = int(input('Enter how many years to pay the house: '))

# quantity months to pay
monthly_payment= house_value / ( years_to_pay * 12) 

# 30% salary
max_payment_allowed = salary * 0.30

print(f'To pay for a house valued at R${house_value:.2f} over {years_to_pay} years, ', end='')
print(f'the monthly payment would be R${monthly_payment:.2f}')

if monthly_payment <= max_payment_allowed:
    print(f'Loan approved {max_payment_allowed}')
else:
    print('Loan denied')
