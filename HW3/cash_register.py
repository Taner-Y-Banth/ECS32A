# cash_register.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Acts as a total counter

# inits variables
total = 0
counter = 0

print("Cash register (press enter to exit)")

# loops until exited
while True:
    inp = input('Enter item cost:')
    if inp != "":
        total += float(inp)
        counter += 1
        continue
    else:
        break

formatted_str = "{:.2f}".format(total) # formats total

print(f'You entered {counter} items totaling ${formatted_str}')