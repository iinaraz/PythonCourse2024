# Rectangle area program

# Define function
def calculate_rectangle():

    width = int(input("Width:"))
    length = int(input("Length:"))

    return("Area of a rectangle:", width * length, "Circumference of a rectangle:", width*2+length*2)

# Save answer to a variable
answer = calculate_rectangle()

# Print answer
print(answer)
