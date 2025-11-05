# Guess the Number Game #

import random
print("Welcome to the Number Guessing Game!")
randomnumber = random.choice(range(1, 100))
player_choice = input("Make a guess: ")
player_choice1 = int(player_choice)
max_attempts = 5
attempts = 0

while player_choice1 != randomnumber:
     if player_choice1 > 100:
        print("You can't guess higher than 100")
     if player_choice1 > randomnumber:
        print("Too high")
        print("Guess Again")
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts left.\n")
        player_choice = input("Make another guess: ")
        player_choice1 = int(player_choice)
     if max_attempts - attempts < 2:
        print(f"You ran out of attempts. Good try. the number was {randomnumber}")
        break
     if player_choice1 < randomnumber:
        print("Too low")
        print("Guess Again")
        attempts += 1
        print(f"You have {max_attempts - attempts} attempts left.\n")
        player_choice = input("Make another guess: ")
        player_choice1 = int(player_choice)
     if player_choice1 == randomnumber:
        print(f"You guessed right! {randomnumber}")
        break
