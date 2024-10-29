# Carla Epperson
# October 29, 2024
# P3LAB
# Calculates the number of dollars and coins needed for a given amount of money.

# Ask the user to enter an amount of money as a float
amount = float(input("Enter the amount of money as a float: $"))

# Convert the amount to cents to work with whole numbers
cents = int(amount * 100)

# Calculate the number of dollars and the remaining cents
dollars = cents // 100
cents %= 100

# Calculate the number of quarters and the remaining cents
quarters = cents // 25
cents %= 25

# Calculate the number of dimes and the remaining cents
dimes = cents // 10
cents %= 10

# Calculate the number of nickels and the remaining cents
nickels = cents // 5
cents %= 5

# The remaining cents are pennies
pennies = cents

# Display the results
if dollars > 0:
    print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
if quarters > 0:
    print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
if dimes > 0:
    print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
if nickels > 0:
    print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
if pennies > 0:
    print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
elif dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0:
    print("No change")
