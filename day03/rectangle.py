# Rectangle area program

# Define variables
width = int(input("Width:"))
length = int(input("Length:"))

# Define function
def calculate_rectangle(width, length):
    return("Area of a rectangle:", width * length, "Circumference of a rectangle:", width*2+length*2)

# Save answer to a variable
answer = calculate_rectangle(width, length)

# Print answer
print(answer)
