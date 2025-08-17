from tkinter import Button
from logique.sommeil import traiter_reponse_sommeil


class AccueilMixin:
    def ecran_accueil(self):
      

        self.afficher_message("👋 Salut Mon Maître") # pyright: ignore[reportAttributeAccessIssue]
        self.afficher_message("👀 Comment tu vas?") # pyright: ignore[reportAttributeAccessIssue]
        self.afficher_message("Tu as bien dormi? 🤔\n") # pyright: ignore[reportAttributeAccessIssue]

        # Boutons Y/N
        btn_oui = Button(
            self.frame_boutons, # pyright: ignore[reportAttributeAccessIssue]
            text="😊 Oui",
            command=lambda: self.repondre_sommeil("y"),
        )
        btn_non = Button(
            self.frame_boutons, # pyright: ignore[reportAttributeAccessIssue]
            text="😴 Non",
            command=lambda: self.repondre_sommeil("n"),
        )

        btn_oui.pack(side="left", padx=10)
        btn_non.pack(side="left", padx=10)

    def repondre_sommeil(self, reponse):
        # Import uniquement ici pour éviter les imports circulaires

        message = traiter_reponse_sommeil(reponse)
        self.afficher_message(message) # pyright: ignore[reportAttributeAccessIssue]

        # Nettoyer les boutons
        for widget in self.frame_boutons.winfo_children(): # pyright: ignore[reportAttributeAccessIssue]
            widget.destroy()

        # Créer un stub temporaire
        self.envoie_message() # pyright: ignore[reportAttributeAccessIssue]
