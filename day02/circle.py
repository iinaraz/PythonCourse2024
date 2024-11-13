# Circle area program

import math

# Define variables
radius = int(input("Radius:"))

def calculate_circle(radius):
    return("Area of the circle:", math.pi * radius**2, "Circumference of the circle:", 2*math.pi*radius)
