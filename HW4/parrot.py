# parrot.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Parrot app

x = ""
while True:
    x = input(">")
    if x.lower() != "quiet":
        y = x.upper()
        print(y)
    else:
            break