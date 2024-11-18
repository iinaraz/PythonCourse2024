# Circle area program

import math

# Define function
def calculate_circle():

    radius = int(input("Radius:"))

    return("Area of the circle:", math.pi * radius**2, "Circumference of the circle:", 2*math.pi*radius)

answer = calculate_circle()
print(answer)