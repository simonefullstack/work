#This is a game to guess the numbers between 0 and 10. The player has 3 tries to guess the correct number.

import random

#generate random number to be guessed
random_num = random.randint(0, 10)

#number of guesses each person gets
num_guess = 3

#for loop to give the three chances to guess and evealuate if number has been guessed.
for i in range(num_guess):
    guess = int(input("What is your guess?"))

    #make sure number is between 0 and 10
    if (guess < 0 or guess > 10):
        print("Guess is invalid. Guess again.")


    # if random number is guessed, break loop and let person know
    if random_num == guess:
        print("Congratulations!! You guessed the number.")
        break

#let user know random number
print("The random number is ", + random_num)
