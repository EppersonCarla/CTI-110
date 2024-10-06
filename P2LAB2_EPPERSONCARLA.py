#Carla Epperson
#October 6, 2024
#P2Lab2
#Dictionary Items

# Create a dictionary with vehicle MPG values
vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado':26 }

#Get all keys from the dictionary
keys= vehicle_mpg.keys()
print(keys) #Will print the keys of the dicitonary

#Have the user enter a vehicle
vehicle = input("Enter a vehicle to see its mpg:")
print()

#Show the mpg for the entered vehicle

if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")
    print()

    # Ask user for the number of miles they will drive
    miles = float(input(f"How may miles will you drive the {vehicle}?"))
    print()

    #Calculate the gallons of gas needed
    gallons_needed = miles / mpg

    #Show the gallons fo gas needed, to the two decimal place
    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")
    
    
