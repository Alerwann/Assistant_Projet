from tkinter import Button

from logique.applications import *


class MenuMixin:
    def menu_principal(self):
        """
        Mise en place de l'interface pour le choix d'activité

        UI Elements:
            - btn1 -> relier à l'action compte
            - btn2 -> relier à l'action jeu
            - btn3 -> relier au choix code
        Action:
            - Propose le choix pour l'action à faire
            - Démarre le tiemer pour le petit déjeuner
            - Relie les choix aux méthodes adéquates

        Note : le timer tourne en arrière plan
        """
        self.show_message(
            "Passons aux choses sérieuses, que veux-tu faire?\n"
        )  # pyright: ignore[reportAttributeAccessIssue]

        # Boutons d'action
        btn1 = Button(
            self.frame_button, text="📊 Comptes", command=self.acccount_action
        )  # pyright: ignore[reportAttributeAccessIssue]
        btn2 = Button(
            self.frame_button, text="🎮 Jeu", command=self.game_action
        )  # pyright: ignore[reportAttributeAccessIssue]
        btn3 = Button(
            self.frame_button, text="💻 Code", command=self.code_action
        )  # pyright: ignore[reportAttributeAccessIssue]

        btn1.pack(side="left", padx=10)
        btn2.pack(side="left", padx=10)
        btn3.pack(side="left", padx=10)

    def acccount_action(self):
        """Lance la logique choice_1 après avoir valider par l'affichage d'un message """
        self.show_message(
            "📊 Ouverture de tes comptes... \n"
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_1()

    def game_action(self):
        """Lance la logique choice_2 après avoir valider par l'affichage d'un message """
        self.show_message(
            "🎮 Tu as raison, commençons en douceur! \n"
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_2()

    def code_action(self):
        """Lance la logique choice_3 après avoir valider par l'affichage d'un message """
        self.show_message(
            "💻 Tu es d'humeur à te concentrer! \n"
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_3()
