from tkinter import Tk,  Button, Text, Frame
import sys
import os
from tkinter import PhotoImage
import time

from .welcome_mixin import WelcomMixin

from .menu_mixin import MenuMixin
from .whatsapp_mixin import WhatsAppMixin


class AssistantGUI(
    WhatsAppMixin,
    WelcomMixin,
    MenuMixin,
):
    def __init__(self):
        """Création de l'ensemble des variables de l'application ainsi que les éléments d'ui"""
        self.fenetre = Tk()
        self.fenetre.title("🤖 Assistant Personnel")
        self.fenetre.geometry("600x500")

        # Zone d'affichage
        self.messages = Text(self.fenetre, height=20, width=70, font=("Arial", 13))
        self.messages.pack(pady=10)

        # Zone boutons
        self.frame_button = Frame(self.fenetre)
        self.frame_button.pack(pady=10)

        # Zone de bouton quitter
        self.frame_quit_button = Frame(self.fenetre)
        self.frame_quit_button.pack(pady=10)

        # Bouton Quitter permanent
        quit_btn = Button(
            self.frame_quit_button, text="❌ Quitter", command=self.quitter_complet
        )
        quit_btn.pack(side="left", padx=10)

        # Changement icon
        try:
            icon_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                "assets",
                "icon_32.png",
            )
            icon = PhotoImage(file=icon_path)
            self.fenetre.iconphoto(True, icon)
        except Exception as e:
            print(f"Impossible de download l'icône : {e}")

        # Démarrer
        self.welcom_screen()  # Méthode héritée d'AccueilMixin
        self.fenetre.mainloop()

    def show_message(self, message):
        self.messages.insert("end", message + "\n")
        self.messages.see("end")

    def quitter_complet(self):
        """Arrête tout, y compris le timer
        note: a ameliorer avec double validation"""
        self.show_message("Tu quittes la page et le timer va être annulé")
        
        import os

        os._exit(0)


if __name__ == "__main__":
    AssistantGUI()
