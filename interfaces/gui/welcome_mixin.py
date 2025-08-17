from tkinter import Button
from logique.sleep import treat_resp_sleep


class WelcomMixin:
    def welcom_screen(self):

        self.show_message(
            "👋 Salut Mon Maître"
        )  # pyright: ignore[reportAttributeAccessIssue]
        self.show_message(
            "👀 Comment tu vas?"
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
