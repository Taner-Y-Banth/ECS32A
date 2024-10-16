# quiz_part1.py
# Ethan Bryant HW2
# ECS32A Dr. Kristian Stevens
# Checks validity of an answer to a question

print(
    "ART: Who painted 'The Persistance of Memory'?\n"
    "a. Dali\n"
    "b. Munch\n"
    "c. Picasso"
    )

userResponse = input("Enter your choice:")

if userResponse == "a":
    print("Correct!")
elif userResponse != "a":
    print("The correct answer was a")