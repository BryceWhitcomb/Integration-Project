# Bryce Whitcomb
# Integration Project: Text Based Game

# Initial Health
initialHealth = int(10)

# Player Health
def playerHealth(initialHealth, takenDamage):
    finalHealth = initialHealth - takenDamage
    if finalHealth <= 0:
        return -5
    else:
        return finalHealth

# Fight
import random
randNum = random.randint(1, 10)
def fight():
    print(playerHealth(initialHealth, randNum))

# Game Introduction
print('Welcome to "Text Based Game!" '
      '\nYou have 10 health, and a chance to take between 1 and 10 damage'
      '\nHow many times can you not get a "Game Over"?')


count = 0
while fight() != -5:
    count = count + 1
print("You survived", count, "time(s)")
