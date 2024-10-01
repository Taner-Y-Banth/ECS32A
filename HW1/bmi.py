# bmi.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Calculates bmi in imperial units

height = float(input("Enter height in inches:"))
weight = float(input("Enter weight in pounds:"))
bmi = (weight / (height ** 2)) * 703 # calculates bmi

print("BMI:", bmi)