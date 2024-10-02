# hybrid.py
# Ethan Bryant HW1 
# ECS32A Dr. Kristian Stevens
# Calculates cost of ownership of a hybrid car

# Defines all inputs and converts them to floating point numbers
costCar = float(input("Cost of car:"))
milesDriven = float(input("Miles driven per year:"))
costGas = float(input("Cost of gas:"))
mpg = float(input("Fuel efficiency (mpg):"))
val = float(input("Estimated resale value after 5 years:"))

# calculates necessary values
fiveYearGas = (costGas * (milesDriven / mpg)) * 5
fiveYearCar = costCar - val

# returns output
print("Five year gas cost:", fiveYearGas)
print("Five year car cost:", fiveYearCar)
print("Five year total cost:", fiveYearGas + fiveYearCar)