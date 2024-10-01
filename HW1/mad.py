# mad.py
# Ethan Bryant HW1
# ECS32A Dr. Kristian Stevens
# Plays a game of madlibs with a user

# collects all necessary inputs from a user
adj = input("Enter an adjective:")
noun = input("Enter a noun:")
plNoun = input("Enter a plural noun:")
place = input("Enter a place:")
partBody = input("Enter a part of the body:")

print("")
print("There are many " + adj + " ways to choose a " + noun + " to read." )
print("You could ask recommendations from your friends and " + plNoun + ".")
print("If they are no help, head to your local library or " + place + " and browse the shelves")
print("until something catches your " + partBody + ".")