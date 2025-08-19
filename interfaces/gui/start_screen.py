from tkinter import Tk,  Button, Text, Frame, ttk
import sys
import os
from tkinter import PhotoImage
import time

from .welcome_mixin import WelcomMixin

from .menu_mixin import MenuMixin
from .whatsapp_mixin import WhatsAppMixin
from .progressbar_mixin import ProgressBarMixin


class AssistantGUI(
    WhatsAppMixin,
    WelcomMixin,
    MenuMixin,
    ProgressBarMixin
):
    def __init__(self):
        """Création de l'ensemble des variables de l'application ainsi que les éléments d'ui"""
        self.fenetre = Tk()
        self.fenetre.title("🤖 Assistant Personnel")
        self.fenetre.geometry("900x700")

        # Zone d'affichage
        self.messages = Text(self.fenetre, height=20, width=110, font=("Arial", 13))
        self.messages.pack(pady=10)

        # Zone boutons
        self.frame_button = Frame(self.fenetre)
        self.frame_button.pack(pady=10)

        # Affichage Zone de de progresse barre
        self.zone_progressbars = Frame(self.fenetre)
        self.zone_progressbars.pack(pady=10)

        #dictionnaire de stocka d'états
        self.progressbars_frame={}
      

        # Zone de bouton quitter
        self.frame_quit_button = Frame(self.fenetre)
        self.frame_quit_button.pack(pady=5)

        # Bouton Quitter permanent
        quit_btn = Button(
            self.frame_quit_button, text="❌ Quitter", command=self.quitter_complet
        )
        quit_btn.pack(side="left", padx=5)

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
