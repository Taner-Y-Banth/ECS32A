# change.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Calculates change from cents

cents = int(input('Enter cents:'))

quarters = cents // 25
dimes = (cents % 25) // 10
nickels = ((cents % 25) % 10) // 5
pennies = ((cents % 25) % 10) % 5


# used an f string, am familiar with formatted strings from javascript
print(f'The minimum coins for {cents} cents are:')
print(f'{quarters} Quarters')
print(f'{dimes} Dimes')
print(f'{nickels} Nickels')
print(f'{pennies} Pennies')