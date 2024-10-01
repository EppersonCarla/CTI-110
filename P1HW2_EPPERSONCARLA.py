#Carla Epperson
#September 30,2024
#P1HW2
#Travel Bugdet and Expenses

print("This program calculates and displays travel expenses")
print()
budget = input("Enter your total budget: ")
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = input("Enter the amount you think you will spend on gas: ")
print()
accommodation_expense = input("Enter the amount you will spend on accommodation/hotel: ")
print()
food_expense = input("Last, Enter the amount you will spend on food: ")
print()

budget = float(budget)
gas_expense = float(gas_expense)
accommodation_expense = float(accommodation_expense)
food_expense = float(food_expense)

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("-----Travel Details-----")
print()
print("Destination:", destination)
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)
