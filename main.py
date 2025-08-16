from interfaces.gui import AssistantGUI


def main():
    app = AssistantGUI()


if __name__ == "__main__":
    main()


# """
# Assistant Personnel - Point d'entrée principal
# Auteur: Alerwann
# """
# from datetime import datetime
# import sys
# import os
# import subprocess
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from interfaces.gui import AssistantGUI

# def main():
#     """
#     Lance l'assistant seulement avant 10h du matin
#     """
# heure_actuelle = datetime.now().hour


# if heure_actuelle > 2:
#     try:
#         app = AssistantGUI()
#     except KeyboardInterrupt:
#         print("\n👋 Assistant fermé par l'utilisateur")
#     except Exception as e:
#         print(f"❌ Erreur lors du lancement: {e}")

# else :


#     print("🕙 Il est trop tard ! L'assistant ne se lance qu'avant 10h du matin.")
#         # Optionnel : afficher une notification

#     subprocess.run([
#             "terminal-notifier",
#             "-title", "Assistant",
#             "-message", "Assistant disponible seulement avant 10h ⏰"
#         ])


# def version_info():
#     """
#     Affiche les informations de version
#     """
#     print("🤖 Assistant Personnel v1.0")
#     print("Interface graphique Tkinter")
#     print("Développé par Alerwann")


# if __name__ == "__main__":
#     main()
