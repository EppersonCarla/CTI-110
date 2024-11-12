# Carla Epperson
# November 12, 2024
# P4HW2
# Decision structures and formatting strings to display nicely
# Enhanced Program to calculate multiple employee's pay based on hours worked and pay rate

"""
Pseudocode:
1. Set up variables for totals and employee count.
2. Loop for each employee:
    a. Get employee name (if "Done", stop).
    b. Get hours worked and pay rate.
    c. Calculate overtime, regular pay, and gross pay.
    d. Update total pay for overtime, regular, and gross.
    e. Show employee pay info.
3. After the loop, show total overtime, regular pay, gross pay, and number of employees.
"""

# Initialize totals and employee count
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    # Get employee name ('Done' ends input)
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break
    
    # Get hours worked and pay rate
    hours_worked = float(input(f"Enter number of hours worked for {employee_name}: "))
    pay_rate = float(input(f"Enter pay rate for {employee_name}: "))
    
    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        overtime_hours = 0
        overtime_pay = 0

    regular_pay = min(hours_worked, 40) * pay_rate
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    # Print individual results
    print("------------------------------------------------")
    print(f"Employee name: {employee_name}")
    print("Hours Worked    Pay Rate    OverTime     OverTime Pay   RegHour Pay      Gross Pay")
    print("------------------------------------------------")
    print(f"{hours_worked:<15.1f} ${pay_rate:<10.2f} {overtime_hours:<10.1f}  ${overtime_pay:<13.2f} ${regular_pay:<13.2f} ${gross_pay:<10.2f}")
    print("------------------------------------------------\n")

# Print totals after all entries
print("\nSummary of Payroll")
print("------------------------------------------------")
print(f"Total number of employees: {employee_count}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
print("------------------------------------------------")
