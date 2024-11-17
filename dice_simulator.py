# dice_simulator.py
import random

def roll_die(sides=6):
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    return [roll_die(sides) for _ in range(num_dice)]

def save_results_to_file(results, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("Rolled dice results:\n")
        file.write(", ".join(map(str, results)))
        file.write("\n")

print("Dice Simulator")
sides = int(input("Enter the number of sides on the die: "))
num_dice = int(input("Enter the number of dice to roll: "))
results = roll_multiple_dice(num_dice, sides)
print(f"Rolled: {results}")
save_results_to_file(results)
print("Results saved to results.txt")
print("End of simulation")
print("Thank you for using the simulator")