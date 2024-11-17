# dice_simulator.py
import random

def roll_die():
    return random.randint(1, 6)

print("Dice simulator")
print(f"Rolled: {roll_die()}") # The function was not called in previous code!