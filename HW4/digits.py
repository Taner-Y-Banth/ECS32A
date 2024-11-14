# digits.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Phone number stripper

x = input("Enter phone number:")
y = ""

for char in x:
    if char.isnumeric():
        y = y + char

print("Digit string:", y)