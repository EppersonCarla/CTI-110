#Carla Epperson
#October 6,02024
#P2LAB1
#Circle Formula

import math

# Get radius from the user as a float
radius = float(input("What is the radius of the circle? "))

# Calculate the diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with the specified formatting

print(f"\nThe diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
