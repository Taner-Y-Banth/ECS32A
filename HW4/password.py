# password.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# Checks for qualities of a password

word = input("Enter password:")

# Checks once for each type
digit = 0
upper = 0
lower = 0
special = 0

if len(word) > 7:
    print("Has length")
# loop over each char in word
for char in word:
	# Check upper and lower case
	if char.islower() and lower == 0:
		lower = 1
	elif char.isupper() and upper == 0:
		upper = 1
	# Check for digit  
	elif char in "0123456789" and digit == 0:
		digit = 1
 	# Check for special  
	elif char in "!@#$%&" and special == 0:
		special = 1

# to maintain order of print statements
if lower == 1:
    print("Has lower case") 
if upper == 1:
	print("Has upper case") 
if digit == 1:
	print("Has digit")
if special == 1:
	print("Has special") 