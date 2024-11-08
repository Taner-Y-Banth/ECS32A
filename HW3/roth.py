# roth.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Calculates interest

# initializes all variables
initial = float(input("Enter an initial Roth IRA deposit amount:"))
rate = int(input("Enter an annual percent rate of return:"))
current = initial
years = 0

while current <= (2 * initial):
    years += 1
    current *= (1 + rate / 100)
    print(f"Value after year {years}: ${current:.2f}") # learned added functionality of f string with inline formatting

print(f"It will take {years} years to double your investment with a {rate}% APR.")