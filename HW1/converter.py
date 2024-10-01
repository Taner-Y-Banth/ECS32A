# converter.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Converts a letter to a binary and numerical representation of itself

input = input("Enter a character:")

print(input + " corresponds to the integer", ord(input), " which is " + bin(ord(input)) + " in binary.")