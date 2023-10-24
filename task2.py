"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random

def title():
    print("Guess the number")
    print("How to play:\nThe Computer will pick a random number from 1 to 100\nThe user will be asked to enter their guess\nThe computer will then tell the user if their guess is lower than or higher than the number the computer has in mind\nThe user gets a maximum of 10 guesses")

def game():
    num = random.randint(1,100)
    guesses = 0
    max_guesses = 10

    while guesses < max_guesses:
        guess = int(input("Enter your guess: ")) 
        if guess == num:
            print(f"Correct! The number was {num}")
            print(f"You won after {10 - guesses} guesses")
            break
        elif guess < num:
            print("Wrong! The number is higher")
            guesses += 1
            continue
        elif guess > num:
            print("Wrong! The number is lower")
            guesses += 1
            continue
    print(f"Game Over! You ran out of guesses, the correct number was {num}.")

title()
game()