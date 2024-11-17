import random
import argparse

def roll_die(sides=6):
    """
    Simule le lancer d'un dé avec un nombre de faces donné.
    
    Paramètres :
        sides (int) : Nombre de faces du dé. Par défaut 6.
        
    Retourne :
        int : Résultat du lancer de dé.
    """
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    """
    Simule le lancer de plusieurs dés avec un nombre de faces donné.
    
    Paramètres :
        num_dice (int) : Nombre de dés à lancer.
        sides (int) : Nombre de faces sur chaque dé. Par défaut 6.
        
    Retourne :
        list : Résultats de tous les lancers de dés.
    """
    return [roll_die(sides) for _ in range(num_dice)]

def save_results_to_file(results, filename="results.txt"):
    """
    Sauvegarde les résultats des lancers de dés dans un fichier.
    
    Paramètres :
        results (list) : Liste des résultats des lancers de dés.
        filename (str) : Nom du fichier de sauvegarde. Par défaut "results.txt".
    """
    with open(filename, "w") as file:
        file.write("Résultats des lancers de dés :\n")
        file.write(", ".join(map(str, results)))
        file.write("\n")

def main():
    """
    Fonction principale pour gérer les arguments de ligne de commande 
    et exécuter le simulateur de dés.
    """
    parser = argparse.ArgumentParser(description="Simulateur de Dés")
    parser.add_argument("--sides", type=int, default=6, help="Nombre de faces du dé")
    parser.add_argument("--num-dice", type=int, default=1, help="Nombre de dés à lancer")
    parser.add_argument("--output", type=str, default="results.txt", help="Fichier de sortie pour les résultats")
    args = parser.parse_args()

    results = roll_multiple_dice(args.num_dice, args.sides)
    print(f"Lancers : {results}")
    save_results_to_file(results, args.output)
    print(f"Résultats sauvegardés dans {args.output}")
    print("Fin de la simulation")
    print("Merci d'avoir utilisé le simulateur")

if __name__ == "__main__":
    main()