# heart.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Calculates estimates of heartrate

age = int(input("Enter your age:"))
maxRate = 220 - age
targetRate = [maxRate * .5, maxRate * .85] # learned in a compsci course in highschool

print("Your maximum heart rate is ", maxRate, " bpm")
print("Your target heart rate is ", targetRate[0], " - ", targetRate[1], " bpm")
