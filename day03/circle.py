# Circle area program

import math
import argparse

# Define function
def calculate_circle(radius):
    
    return(f"Area of the circle: {math.pi * radius**2} Circumference of the circle: {2*math.pi*radius}")

parser = argparse.ArgumentParser()
parser.add_argument("--radius", help="Radius of the circle", type = int, required = True)
args = parser.parse_args()

print(calculate_circle(args.radius))