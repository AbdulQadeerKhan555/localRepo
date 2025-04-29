4# Guess the number game
# This is a simple number guessing game where the user has to guess a number between 0 and 99.
# The user has 5 attempts to guess the number correctly. If the guess is too low or too high, the program will provide feedback.    
import random
print("Number Guessing Game! ")
guess: int

#Generating random number.
number = random.randint(0, 99)
# Five attempt should be allowed
attempt: int = 5

# Using while condition for loop.
while(attempt >= 0):
    #Get user input about guess
    guess = input("Enter you guess!  ")
    guess = int(guess)

    if(guess < number):
        print("Your guess is too low! ")
    elif(guess > number):
        print("Your guess is too high")
    elif(guess == number):
        print("Congraturations your guess is correct!")
        break
    else:
        print("Enter the right input!")
    # Decrement the attempt by 1
    attempt -= 1
    print("You have ", attempt, " attempts left!")
    if(attempt == 0):
        print("You have no attempts left!")
        print("The number was ", number)
        break