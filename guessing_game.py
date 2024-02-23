"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Written by Philip Garner
#   02/23/2024



import random

derogatory_list = ["mortal", "nimwhit", "nincun-poop", "muggler", "bassoon player", "drug lord",
                   "python-tester", "n3rd"]


def start_game():
    print("""Welcome player one, to this number guessing game
It is important that you concentrate and try to guess the number
using as few attempts as possible! The fewer attempts, the better!
...
I cannot stress this enough! The fate of the world lies in your hands
        """)
    random_number = random.randrange(11)
    attempt_counter = 1
    while True:
        derogatory = random.choice(derogatory_list)
        try:
            if attempt_counter == 1:
                guess = int(input(f"Guess, {derogatory} >    "))
            else:
                guess = int(input(f"Guess again, {derogatory} >    "))
                
            if guess == random_number:
                print(f"""Congratulations, you saved the world in {attempt_counter} attempts!
Tune in again tomorrow for the next catastrophe!
""")
                break

            elif guess > 10:
                    print(f"Your guess was too high, don't squander it, {derogatory}")
            elif guess < 0:
                    print(f"Your guess was too low........ {derogatory}")
            elif guess < random_number:
                print("That guess was too low!")
                attempt_counter += 1
            elif guess > random_number:
                print("That guess was too high!")
                attempt_counter += 1
        except ValueError as e:
            print(f"That's not a valid number, you {derogatory}!")


start_game()

# Thank you for checking my code
