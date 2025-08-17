# """
# Assistant Personnel - Point d'entrée principal
# Auteur: Alerwann

from interfaces.gui import AssistantGUI
from interfaces.cli import assistant_cli


def main():
    """Choix du type d'interface graphique ou non et début du main"""
    print("=== Mon Application ===")
    print("Choisissez le mode d'interface :")
    print("1. Interface en ligne de commande (CLI)")
    print("2. Interface graphique (GUI)")

    while True:
        try:
            choice = input("Votre choice (1 ou 2) : ").strip()

            if choice == "1":
                print("Lancement du mode CLI...")
                assistant_cli()
                break
            elif choice == "2":
                print("Lancement du mode GUI...")
                AssistantGUI()
                break
            else:
                print("choice invalide. Veuillez entrer 1 ou 2.")

        except KeyboardInterrupt:
            print("\nAu revoir !")
            break


if __name__ == "__main__":
    main()
