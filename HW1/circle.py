# circle.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Calculates dimensions of a given circle

rad = float(input("Enter radius:"))
diameter = rad * 2
pi = 3.14159

print("Diameter", diameter)
print("Circumference", pi * diameter) 
print("Area", pi * (rad ** 2))