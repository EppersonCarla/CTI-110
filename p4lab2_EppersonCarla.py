#Carla Epperson
#October 30,2024
#P4LAB2
#Display Information to user using loops

"""
Program: Program Running with positive integer input

1. Use a loop to keep the program running until the user decides to exit.
2. Ask the user to enter an integer.
3. If the number is negative:
   - Inform the user that negative numbers are not accepted.
4. If the number is zero or positive:
   -display the multiplication table for that number.
5. Ask the user if they want to run the program again.
6. Handle errors if the input is not an integer.
"""

def display_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):  
        print(f"{number} x {i} = {number * i}")

def main():
    while True: 
        try:
            user_input = int(input("Enter an integer: "))
            if user_input < 0:
                print("This program does not handle negative numbers")
            else:
                display_multiplication_table(user_input)

            
            run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
            if run_again != 'yes':
                print("Exiting program....")
                break  
        except ValueError:
            print("Error. Please enter an integer")

if __name__ == "__main__":
    main()
