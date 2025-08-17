from tkinter import Button
from logique.notification import send_30min_timer
from logique.applications import *


class MenuMixin:
    def menu_principal(self):
        self.show_message(
            "\nPassons aux choses sérieuses, que veux-tu faire?\n"
        )  # pyright: ignore[reportAttributeAccessIssue]

        # Lancer le timer
        send_30min_timer()

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
        self.show_message(
            "📊 Ouverture de tes comptes..."
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_1()

    def game_action(self):
        self.show_message(
            "🎮 Tu as raison, commençons en douceur!"
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_2()

    def code_action(self):
        self.show_message(
            "💻 Tu es d'humeur à te concentrer!"
        )  # pyright: ignore[reportAttributeAccessIssue]
        choice_3()
