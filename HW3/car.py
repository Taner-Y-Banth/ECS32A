# car.py
# Ethan Bryant HW3
# ECS32A Dr. Kristian Stevens
# Uses a loop to play a guessing game

price = 44500
guesses = 0

print("Guess the price and win the prize!")

while True:
    guess = int(input("Enter your guess:"))
    guesses += 1
    
    if guess == price:
        break # the win condition
    elif guess < price:
        print("Too low!")
    else:
        print("Too high!")

if guesses <= 5:
    print(f"It took {guesses} guesses.")
    print("You won the car!")
else:
    print(f"It took {guesses} guesses.")
    print("Too many guesses!")
