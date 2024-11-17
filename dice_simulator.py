# dice_simulator.py
import random

def roll_die(sides=6):
    return random.randint(1, sides)

print("Dice simulator")
sides = int(input("Enter the number of sides on the die: "))
print(f"Rolled: {roll_die(sides)}")