
import random

def guess_the_number():
    win = False
    name = input("Hello! What is your name?")
    number = random.randint(1,10000)
    print(f"Well, {name}, I am thinking of a number between 1 and 10000.")
    count = 0
    while win is False:
        count += 1
        guess = int(input("Take a guess:"))
        if guess < number:
            print("Your number is too low.")
        elif guess > number: 
            print("Your number is too high.")
        elif guess == number:
            print(f"Good Job, {name}! You guessed my number in {count} guesses!")
            win = True
            replay = input("Would you like to play again (Y/N)?")
            if replay == "Y":
                guess_the_number()

guess_the_number()