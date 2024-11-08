# mileage.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# mileage

print("Your Personal Fuel Economy")

# inits variables
gallons = 0
miles = 0
mileage_total = 0
i = 0

while True:
    miles_input = input("Number of miles traveled (or enter to exit):")
    
    if miles_input == "": # exits loop
        break
    
    gallons_input = input("Number of gallons needed:")
    
    miles = float(miles_input)
    gallons = float(gallons_input)
    
    mileage = miles / gallons
    mileage_total += mileage
    i += 1
    print(f"Mileage this tank = {mileage:.1f}")

if gallons > 0:
    average_mileage = mileage_total / i
    print(f"Average mileage = {average_mileage:.1f}")
else:
    print("No gallons entered; cannot calculate average mileage.")