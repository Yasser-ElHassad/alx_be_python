month_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))

month_saving = month_income - total_expenses

annual_interest = 0.05

projected_saving = month_saving * 12 + (month_saving * 12 * annual_interest)

print(f'Your monthly savings are ${month_saving}')
print(f'Projected savings after one year, with interest, is: ${int(projected_saving)}.')

