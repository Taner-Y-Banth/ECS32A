# quiz_part4.py
# Ethan Bryant HW2
# ECS32A Dr. Kristian Stevens
# Adds Genius Question

score = 0 # inits score to 0

print(
    "ART: Who painted 'The Persistance of Memory'?\n"
    "a. Dali\n"
    "b. Munch\n"
    "c. Picasso"
    )

userResponse = input("Enter your choice:")

if userResponse == "a":
    score += 1
    print("Correct!")
else:
    print("The correct answer was a")
    
print(
    "ENTERTAINMENT: How many oscars did Hitchcock win?\n"
    "a. None\n"
    "b. One\n"
    "c. Two"
    )

userResponse = input("Enter your choice:")

if userResponse == "a":
    score += 1
    print("Correct!")
else:
    print("The correct answer was a")
    
print(
    "SCIENCE: Which dinosaur is most closely related to the pelican?\n"
    "a. Velociraptor\n"
    "b. Stegosaurus\n"
    "c. Pterodactyl"
    )

userResponse = input("Enter your choice:")

if userResponse == "a":
    score += 1
    print("Correct!")
else:
    print("The correct answer was a")
    
print(
    "HISTORY: Which of the following was not invented in Baja California?\n"
    "a. Margaritas\n"
    "b. Chocolate\n"
    "c. Caesar Salad"
    )

userResponse = input("Enter your choice:")

if userResponse == "b":
    score += 1
    print("Correct!")
else:
    print("The correct answer was b")
    
print(
    "SCIENCE AND NATURE: Can pigs swim?\n"
    "a. Yes\n"
    "b. No\n"
    "c. Only in salt water"
    )

userResponse = input("Enter your choice:")

if userResponse == "a":
    score += 1
    print("Correct!")
else:
    print("The correct answer was a")
    
print(
    "SPORT AND LEISURE: What color is the middle Olympic ring?\n"
    "a. Red\n"
    "b. Blue\n"
    "c. Black"
    )

userResponse = input("Enter your choice:")

if userResponse == "c":
    score += 1
    print("Correct!")
else:
    print("The correct answer was c")
    
print("Your total score is", score)

print("GENIUS: In ancient Rome, what is L divided by X?")

userResponse = input("Enter your answer:")

if userResponse == "5" or userResponse == "V":
    print("Correct!")
else:
    print("Correct answers were 5 or V")