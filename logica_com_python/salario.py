print(f'{'New Salary':*^50}')

current_salary= float(input('Enter your current salary value: '))

raise_percentage = 0.15 
# or 15/100

new_salary = current_salary + (current_salary * raise_percentage)

print(f'the New Salary is: {new_salary:.2f}')
