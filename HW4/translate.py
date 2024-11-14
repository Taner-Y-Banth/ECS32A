# translator.py
# Ethan Bryant HW4
# ECS32A Dr. Kristian Stevens
# pig latin translator

# input
word = input("Enter a word:").lower()

vowels = "aeiou"

# check initial char
if word[0] in vowels:
    pigLatin = word + "way"
else:
    # creates new string by splicing string
    pigLatin = word[1:] + word[0] + "ay"

# print
print(word, "in Pig latin is", pigLatin)
