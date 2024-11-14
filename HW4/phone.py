# phone.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Phone number validator

y1 = 0
y2 = 0
y3 = 0

x = input("Enter number as ### ###-####:")
x1 = x[0:3]
x2 = x[4:7]
x3 = x[8:12]

for char in x1:
    if char.isnumeric():
            y1 += 1
            
for char in x2:
    if char.isnumeric():
            y2 += 1
            
for char in x3:
    if char.isnumeric():
            y3 += 1
            
if y1 == 3 and y2 == 3 and y3 == 4 and x[3] == " " and x[7] == "-":
    print("Valid")
else:
    print("Invalid")