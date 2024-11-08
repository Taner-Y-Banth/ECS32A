# tip.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Calculates tips


total = float(input("Enter total:"))

# 15-25 is the range
for i in range(15, 26): 
    pct = i/100
    tip = pct * total
    formatted_str = "{:.2f}".format(tip) # formats to two decimal places
    print(f"A {i}% tip is ${formatted_str}")