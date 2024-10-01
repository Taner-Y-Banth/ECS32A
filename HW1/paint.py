# paint.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Calculates amount of cans of paint needed to cover a room

import math # learned in CS class, wanted to utilize ceiling function

length = float(input("Paint coverage estimator\nLength of room in inches:"))
width = float(input("Width of room in inches:"))
avgHeight = float(input("Average height of room in inches:"))
cans = (((length * avgHeight)+(width * avgHeight)) / 72) / 100

print("You'll want", math.ceil(cans), "cans.") # utilizes ceiling function which functions in a similar way to "//" floor division

# Alternate without math package
# 
# length = float(input("Paint coverage estimator\nLength of room in inches:"))
# width = float(input("Width of room in inches:"))
# avgHeight = float(input("Average height of room in inches:"))
# cans = (((((length * avgHeight)+(width * avgHeight)) / 72) / 100) // 1) + 1

# print("You'll want ", int(cans), " cans.")