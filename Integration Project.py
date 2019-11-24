__author__ = "Bryce Whitcomb"
# Text Based Game

# Initial Health
initialHealth = int(10)


# Player Health
def playerHealth(initialHealth, takenDamage):
    initialHealth = initialHealth - takenDamage
    return initialHealth


# Fight
import random


def fight():
    randomNum = int(random.randint(1, 10))
    if randomNum != 10:
        print("Remaining health is", int(playerHealth(initialHealth, randomNum)))
    else:
        return 0


# Game Introduction
print('Welcome to "Text Based Game!" '
      '\nYou have 10 health, and a chance to take between 1 and 10 damage'
      '\nHow many times can you not get a "Game Over"?')

# Main
print("Enter 'y' to begin or any other key to stop.")
begin = input()
if begin == "y":
    play = True
elif begin == "Y":
    play = True
else:
    play = False
count = 0
while play is True:
    if fight() == 0:
        play = False
        print("Game Over.")
    else:
        count = count + 1
        print("You survived! Enter 'y' to play again, or any other key to stop.")
        playAgain = input()
        if playAgain == "y":
            play = True
        elif playAgain == "Y":
            play = True
        else:
            play = False
print("You survived", count, "time(s)")
