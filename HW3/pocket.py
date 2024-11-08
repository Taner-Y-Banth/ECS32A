# pocket.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Calculates value of pocket change

print("Compute your pocket change!")

quarter = int(input("Quarters?"))
dime = int(input("Dimes?"))
nickel = int(input("Nickels?"))
penny = int(input("Pennies?"))

# summation of values
amount = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)

# formats a string
formatted_str = "${:.2f}".format(amount)

print("The total is", formatted_str)