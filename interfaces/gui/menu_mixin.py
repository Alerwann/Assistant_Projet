from tkinter import Button
from logique.notification import lancer_timer_30min
from logique.applications import *

class MenuMixin:
    def menu_principal(self):
        self.afficher_message("\nPassons aux choses sérieuses, que veux-tu faire?\n") # pyright: ignore[reportAttributeAccessIssue]

        # Lancer le timer
        lancer_timer_30min()

        # Boutons d'action
        btn1 = Button(
            self.frame_boutons, text="📊 Comptes", command=self.action_comptes # pyright: ignore[reportAttributeAccessIssue]
        )
        btn2 = Button(self.frame_boutons, text="🎮 Jeu", command=self.action_jeu) # pyright: ignore[reportAttributeAccessIssue]
        btn3 = Button(self.frame_boutons, text="💻 Code", command=self.action_code) # pyright: ignore[reportAttributeAccessIssue]

        btn1.pack(side="left", padx=10)
        btn2.pack(side="left", padx=10)
        btn3.pack(side="left", padx=10)

    def action_comptes(self):
        self.afficher_message("📊 Ouverture de tes comptes...") # pyright: ignore[reportAttributeAccessIssue]
        choix_1()

    def action_jeu(self):
        self.afficher_message("🎮 Tu as raison, commençons en douceur!") # pyright: ignore[reportAttributeAccessIssue]
        choix_2()

    def action_code(self):
        self.afficher_message("💻 Tu es d'humeur à te concentrer!") # pyright: ignore[reportAttributeAccessIssue]
        choix_3()
