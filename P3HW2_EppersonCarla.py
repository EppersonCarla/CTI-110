# Carla Epperson
# October 30,2024
# P3HW2
# Decision structures and formatting strings to display nicely
# Program to calculate employee's pay based on hours worked and pay rate

"""
Pseudocode:
1. Get employee name
2. Get number of hours worked
3. Get pay rate

4. If hours worked is more than 40:
    a. Calculate overtime hours (hours - 40)
    b. Calculate overtime pay (overtime hours * pay rate * 1.5)
5. Else:
    a. Set overtime pay to 0

6. Calculate regular pay (minimum of hours worked and 40 * pay rate)
7. Calculate gross pay (regular pay + overtime pay)

8. Print employee name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay
"""

# Get employee name
employee_name = input("Enter employee's name: ")

# Get number of hours worked
hours_worked = float(input("Enter number of hours worked: "))

# Get pay rate
pay_rate = float(input("Enter employee's pay rate: "))

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_hours = 0
    overtime_pay = 0

# Calculate regular pay
regular_pay = min(hours_worked, 40) * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Print results
print("------------------------------------------------")
print(f"Employee name: {employee_name}")
print("Hours Worked    Pay Rate    OverTime     OverTime Pay   RegHour Pay      Gross Pay")
print("------------------------------------------------")
print(f"{hours_worked:<15.1f} ${pay_rate:<10.2f} {overtime_hours:<10.1f}  ${overtime_pay:<13.2f} ${regular_pay:<13.2f} ${gross_pay:<10.2f}")
print("------------------------------------------------")
