from tkinter import ttk, Label, Button, Frame, Checkbutton, IntVar
import threading
from datetime import timedelta, datetime
import time

from logique.planning import send_whatsapp
from logique.notification import send_timer


class WhatsAppMixin:
    def send(self):
        """
        Création de la fenêtre pour l'envoi du message whatsapp

        UI Elements :
            - btnCheck -> case à coché
            - hour_combo ->comboBox pour le choix des H de 0 à 24
            - minute_combo -> combobox pour le choix des minutes de 5 en 5 de 0 à 55
            - btn_send -> envoie les données choisies

        Action :
            - Nettoie l'interface précédente
            - Renvoie du choix entre immédiat ou l'heure de programmation d'envoie
            - Relie les actions aux méthodes correspondantes

        Note:
            La checkbox active/désactive automatiquement les champs horaires

        """
        for widget in self.frame_button.winfo_children():
            widget.destroy()

        self.show_message("Très bien")
        self.show_message(
            "Quand veux tu l'envoyer? \n"
        )  # pyright: ignore[reportAttributeAccessIssue]

        self.send_now = IntVar()

        # Checkbox "Maintenant"
        btnCheck = Checkbutton(
            self.frame_button,  # pyright: ignore[reportAttributeAccessIssue]
            text="📤 Maintenant",
            variable=self.send_now,
            command=self.toggle_horaire,  # Active/désactive les champs
        )
        btnCheck.pack(pady=10)

        # Frame pour les champs heure/minute
        self.frame_horaire = Frame(
            self.frame_button
        )  # pyright: ignore[reportAttributeAccessIssue]
        self.frame_horaire.pack(pady=10)

        # Label + champ heure
        Label(self.frame_horaire, text="Ou programmer pour :").pack(side="left")

        self.hour_combo = ttk.Combobox(
            self.frame_horaire,
            width=3,
            values=[f"{h:02d}" for h in range(24)],  # 00, 01, 02... 23
            state="readonly",  # Empêche la saisie manuelle
        )
        self.hour_combo.pack(side="left", padx=5)
        self.hour_combo.set("12")  # Valeur par défaut

        Label(self.frame_horaire, text="h").pack(side="left")

        # Menu déroulant minutes (0, 15, 30, 45 ou tous les 5 min)
        self.minute_combo = ttk.Combobox(
            self.frame_horaire,
            width=3,
            values=[f"{m:02d}" for m in range(0, 60, 5)],  # 00, 15, 30, 45
            # Ou pour toutes les 5 min : range(0, 60, 5)
            state="readonly",
        )
        self.minute_combo.pack(side="left", padx=5)
        self.minute_combo.set("00")  # Valeur par défaut

        # Bouton final
        btn_send = Button(
            self.frame_button, text="✉️ Envoyer", command=self.send_exec
        )  # pyright: ignore[reportAttributeAccessIssue]
        btn_send.pack(pady=10)

    def toggle_horaire(self):
        """
        Rend les cases de saisis des heures et minutes inactives si 'maintenant' est sélectionné

        Actions:
            - Si "maintenant"est sélectionné -> champs de saisie désactivées
            - Sinon -> champs de saisie activé
        """
        if self.send_now.get():
            self.hour_combo.config(state="disabled")
            self.minute_combo.config(state="disabled")
        else:
            self.hour_combo.config(state="readonly")
            self.minute_combo.config(state="readonly")

    def send_exec(self):
        """
        Envoie du message selon le choix horaire
        Crée un wigget pour déactiver les boutons de l'interface le temps de l'envoie du message

        Action:
            - Si l'utilisateur veut envoyer immédiatement création du widget et envoie du message
            -Si l'utilisateur souhaite différer enregistrement de l'heure d'envoie et création de timer

        Note : Le timer est créé dans differ_send
        """
        if self.send_now.get():
            # IMMÉDIATEMENT afficher le message d'attente
            self.show_message(
                "⏳ Envoi en cours, veuillez patienter... \n"
            )  # pyright: ignore[reportAttributeAccessIssue]

            # Désactiver le bouton pour éviter les clics multiples
            for (
                widget
            ) in (
                self.frame_button.winfo_children()
            ):  # pyright: ignore[reportAttributeAccessIssue]
                if isinstance(widget, Button):
                    widget.config(state="disabled")

            # Forcer l'affichage immédiat
            self.fenetre.update()  # pyright: ignore[reportAttributeAccessIssue]

            try:

                send_whatsapp()
                self.show_message(
                    "✅ Message envoyé avec succès ! \n"
                )  # pyright: ignore[reportAttributeAccessIssue]
            except Exception as e:
                self.show_message(
                    f"❌ Erreur : {e}"
                )  # pyright: ignore[reportAttributeAccessIssue]

                # Retour menu après 2 secondes
            self.fenetre.after(
                2000, self.back_menu
            )  # pyright: ignore[reportAttributeAccessIssue]
        else:
            heure = int(self.hour_combo.get())
            minute = int(self.minute_combo.get())

            self.show_message(
                f"⏰ Message programmé pour {heure:02d}h{minute:02d} \n"
            )  # pyright: ignore[reportAttributeAccessIssue]
            self.send_programmation(heure, minute)

            self.show_message(
                "✅ Message programmé pour l'envoi ! \n"
            )  # pyright: ignore[reportAttributeAccessIssue]
            self.fenetre.after(
                2000, self.back_menu
            )  # pyright: ignore[reportAttributeAccessIssue]

    def send_programmation(self, heure, minute):
        """
        Lance un timer pour l'envoi différé du message.

        Args:
            heure (int): Heure d'envoi (0-23)
            minute (int): Minute d'envoi (0-59)

        Note:
            Utilise un thread séparé pour ne pas bloquer l'interface
        """
        # Timer en thread séparé
        threading.Thread(
            target=self._differ_send, args=(heure, minute), daemon=True
        ).start()

    def _differ_send(self, heure, minute):
        """
        Suite à une demande d'envoie différé création du timer et envoie du message

        Action :
            - Calcule la différence d'heure entre celle demandé et l'heure de la demande
            - Vérifie si c'est dans la même journée
            - Débute le timer
            - Envoie le message à la fin du timer

        """
        # Calculer l'heure cible aujourd'hui
        now = datetime.now()
        hour_target = now.replace(hour=heure, minute=minute, second=0, microsecond=0)

        # Si l'heure est déjà passée, programmer pour demain
        if hour_target <= now:
            hour_target += timedelta(days=1)
            self.show_message(
                f"⏰ Heure passée, programmé pour demain {heure:02d}h{minute:02d} \n"
            )  # pyright: ignore[reportAttributeAccessIssue]

        # Calculer le délai en secondes
        delay = (hour_target - now).total_seconds()
        send_timer(delay - 30, "whatsapp")
        self.create_progressBar("l'envoie de message", delay)
        # Attendre le délai
        time.sleep(delay)

        # Envoyer le message
        try:

            send_whatsapp()
            self.show_message(
                "✅ Message programmé envoyé !"
            )  # pyright: ignore[reportAttributeAccessIssue]
            self.fenetre.after(
                2000, self.back_menu
            )  # pyright: ignore[reportAttributeAccessIssue]
        except Exception as e:
            self.show_message(
                f"❌ Erreur envoi : {e}"
            )  # pyright: ignore[reportAttributeAccessIssue]

    def send_message(self):
        """
        Affichage des boutons de choix pour envoie du message

        UI Elements:
            yes_btn -> bouton pour répondre "oui"
            no_btn -> bouton pour répondre "non"

        Action :
            - Demande si l'utilisateur veut envoyer le message
            - Relie les choix aux méthodes correspondantes
        """
        self.show_message(
            "Veux-tu envoyer le message du jour? \n"
        )  # pyright: ignore[reportAttributeAccessIssue]

        yes_btn = Button(
            self.frame_button,  # pyright: ignore[reportAttributeAccessIssue]
            text="😊 Oui",
            command=lambda: self.send(),
        )
        no_btn = Button(
            self.frame_button,  # pyright: ignore[reportAttributeAccessIssue]
            text="😟 non",
            command=lambda: self.not_send(),
        )
        yes_btn.pack(side="left", padx=10)
        no_btn.pack(side="left", padx=10)

    def not_send(self):
        """
        Message inscrit pour le non envoie et réinitialisation de la fenêtre

        Actions :
            - Affiche le message confirmant que l'on passe l'action
            - réinitialise la fenêtre
        """
        self.show_message(
            "D'accord on va s'en passer 😒"
        )  # pyright: ignore[reportAttributeAccessIssue]
        self.fenetre.after(
            100, self.back_menu
        )  # pyright: ignore[reportAttributeAccessIssue]

    def back_menu(self):
        """
        Suite à la partie message passage à l'ecran "menu"

        Action :
            - Réinitialise les boutons
            - Relie à la méthode menu
        """
        # Nettoyer tous les boutons actuels
        for (
            widget
        ) in (
            self.frame_button.winfo_children()
        ):  # pyright: ignore[reportAttributeAccessIssue]
            widget.destroy()

        # Recréer le menu principal
        self.menu_principal()  # type: ignore>
