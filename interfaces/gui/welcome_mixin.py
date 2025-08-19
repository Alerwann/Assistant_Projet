from tkinter import Button
from logique.sleep import treat_resp_sleep
from logique.notification import send_timer

from config import BREAKFAST_TIMER_SECOND

class WelcomMixin:
    def welcom_screen(self):
        """
        L'assistant demande pour accueillir si la personne à bien dormi

        UI Elements : 
            - yes_btn -> répond "oui" 
            - no_btn -> répond "non" 

        Actions:
            Relie la réponse à une phrase sympathique
        """
        # Lancer le timer
        send_timer(BREAKFAST_TIMER_SECOND, "breakfast")
        self.create_progressBar('petit déjeuner', BREAKFAST_TIMER_SECOND)

        self.show_message(
            "👋 Salut Mon Maître  \n"
        )  # pyright: ignore[reportAttributeAccessIssue]
        self.show_message(
            "👀 Comment tu vas? \n"
        )  # pyright: ignore[reportAttributeAccessIssue]
        self.show_message(
            "Tu as bien dormi? 🤔\n"
        )  # pyright: ignore[reportAttributeAccessIssue]

        # Boutons Y/N
        yes_btn = Button(
            self.frame_button,  # pyright: ignore[reportAttributeAccessIssue]
            text="😊 Oui",
            command=lambda: self.rep_sleep("y"),
        )
        no_btn = Button(
            self.frame_button,  # pyright: ignore[reportAttributeAccessIssue]
            text="😴 Non",
            command=lambda: self.rep_sleep("n"),
        )

        yes_btn.pack(side="left", padx=10)
        no_btn.pack(side="left", padx=10)

    def rep_sleep(self, reponse):
        """
        Affiche le message en fonction de la réponse de sur le sommeil l'utilisateur

        Actions:
            - Recueil la réponse et traite
            - Nettoie les boutons
            - Relie à la méthode send_message
            
        """
        # Import uniquement ici pour éviter les imports circulaires

        message = treat_resp_sleep(reponse)
        self.show_message(message)  # pyright: ignore[reportAttributeAccessIssue]

        # Nettoyer les boutons
        for (
            widget
        ) in (
            self.frame_button.winfo_children()
        ):  # pyright: ignore[reportAttributeAccessIssue]
            widget.destroy()

        # Créer un stub temporaire
        self.send_message()  # pyright: ignore[reportAttributeAccessIssue]
