# dice_simulator.py
import random
import argparse

def roll_die(sides=6):
    """
    Simulate rolling a single die with a given number of sides.
    
    Parameters:
        sides (int): Number of sides on the die. Default is 6.
        
    Returns:
        int: Result of the die roll.
    """
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    """
    Simulate rolling multiple dice with a given number of sides.
    
    Parameters:
        num_dice (int): Number of dice to roll.
        sides (int): Number of sides on each die. Default is 6.
        
    Returns:
        list: Results of all the dice rolls.
    """
    return [roll_die(sides) for _ in range(num_dice)]

def save_results_to_file(results, filename="results.txt"):
    """
    Save the results of dice rolls to a file.
    
    Parameters:
        results (list): List of results from dice rolls.
        filename (str): Name of the file to save results. Default is "results.txt".
    """
    with open(filename, "w") as file:
        file.write("Rolled dice results:\n")
        file.write(", ".join(map(str, results)))
        file.write("\n")

def main():
    """
    Main function to handle command line arguments and run the dice simulator.
    """
    parser = argparse.ArgumentParser(description="Dice Simulator")
    parser.add_argument("--sides", type=int, default=6, help="Number of sides on the die")
    parser.add_argument("--num-dice", type=int, default=1, help="Number of dice to roll")
    parser.add_argument("--output", type=str, default="results.txt", help="Output file for results")
    args = parser.parse_args()

    results = roll_multiple_dice(args.num_dice, args.sides)
    print(f"Rolled: {results}")
    save_results_to_file(results, args.output)
    print(f"Results saved to {args.output}")
    print("End of simulation")
    print("Thank you for using the simulator")

if __name__ == "__main__":
    main()