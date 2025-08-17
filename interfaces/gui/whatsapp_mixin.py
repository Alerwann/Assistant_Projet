from tkinter import ttk, Label, Button, Frame, Checkbutton,  IntVar
import threading
from datetime import timedelta, datetime
import time

from logique.planning import envoyer_whatsapp


class WhatsAppMixin:
    def envoie(self): 
        for widget in self.frame_boutons.winfo_children(): # pyright: ignore[reportAttributeAccessIssue]
            widget.destroy()

        self.afficher_message("Très bien") # pyright: ignore[reportAttributeAccessIssue]
        self.afficher_message("Quand veux tu l'envoyer?") # pyright: ignore[reportAttributeAccessIssue]

        self.envoi_maintenant = IntVar()

        # Checkbox "Maintenant"
        btnCheck = Checkbutton(
        self.frame_boutons,  # pyright: ignore[reportAttributeAccessIssue]
        text="📤 Maintenant", 
        variable=self.envoi_maintenant,
        command=self.toggle_horaire  # Active/désactive les champs
        )
        btnCheck.pack(pady=10)

        # Frame pour les champs heure/minute
        self.frame_horaire = Frame(self.frame_boutons) # pyright: ignore[reportAttributeAccessIssue]
        self.frame_horaire.pack(pady=10)

        # Label + champ heure
        Label(self.frame_horaire, text="Ou programmer pour :").pack(side="left")

        self.heure_combo = ttk.Combobox(
        self.frame_horaire, 
        width=3,
        values=[f"{h:02d}" for h in range(24)],  # 00, 01, 02... 23
        state="readonly"  # Empêche la saisie manuelle
        )
        self.heure_combo.pack(side="left", padx=5)
        self.heure_combo.set("12")  # Valeur par défaut

        Label(self.frame_horaire, text="h").pack(side="left")

        # Menu déroulant minutes (0, 15, 30, 45 ou tous les 5 min)
        self.minute_combo = ttk.Combobox(
        self.frame_horaire,
        width=3,
        values=[f"{m:02d}" for m in range(0, 60, 5)],  # 00, 15, 30, 45
        # Ou pour toutes les 5 min : range(0, 60, 5)
        state="readonly"
        )
        self.minute_combo.pack(side="left", padx=5)
        self.minute_combo.set("00")  # Valeur par défaut

        # Bouton final
        btn_envoyer = Button(self.frame_boutons, text="✉️ Envoyer", command=self.executer_envoi) # pyright: ignore[reportAttributeAccessIssue]
        btn_envoyer.pack(pady=10)

        # btn_quitter = Button(
        #     self.frame_quit_button, text="❌ Quitter", command=self.quitter_complet # pyright: ignore[reportAttributeAccessIssue]
        # )
        # btn_quitter.pack(side="left", padx=10)

    def toggle_horaire(self):

        if self.envoi_maintenant.get():
            self.heure_combo.config(state="disabled")
            self.minute_combo.config(state="disabled")
        else:
            self.heure_combo.config(state="readonly")
            self.minute_combo.config(state="readonly")

    def executer_envoi(self):

        if self.envoi_maintenant.get():
            # IMMÉDIATEMENT afficher le message d'attente
            self.afficher_message("⏳ Envoi en cours, veuillez patienter...") # pyright: ignore[reportAttributeAccessIssue]

            # Désactiver le bouton pour éviter les clics multiples
            for widget in self.frame_boutons.winfo_children(): # pyright: ignore[reportAttributeAccessIssue]
                if isinstance(widget, Button):
                    widget.config(state="disabled")

            # Forcer l'affichage immédiat
            self.fenetre.update() # pyright: ignore[reportAttributeAccessIssue]

            try:
                
                envoyer_whatsapp()
                self.afficher_message("✅ Message envoyé avec succès !") # pyright: ignore[reportAttributeAccessIssue]
            except Exception as e:
                self.afficher_message(f"❌ Erreur : {e}") # pyright: ignore[reportAttributeAccessIssue]

                # Retour menu après 2 secondes
            self.fenetre.after(2000, self.retour_menu) # pyright: ignore[reportAttributeAccessIssue]
        else:
            heure = int(self.heure_combo.get())
            minute = int(self.minute_combo.get())

            self.afficher_message(f"⏰ Message programmé pour {heure:02d}h{minute:02d}") # pyright: ignore[reportAttributeAccessIssue]
            self.programmer_envoi(heure, minute)

            self.afficher_message("✅ Message programmé envoyé !") # pyright: ignore[reportAttributeAccessIssue]
            self.fenetre.after(2000, self.retour_menu)  # pyright: ignore[reportAttributeAccessIssue]

    def programmer_envoi(self, heure, minute):
        # Timer en thread séparé
        threading.Thread(target=self._envoi_differe, args=(heure, minute), daemon=True).start()

    def _envoi_differe(self, heure, minute):
        # Calculer l'heure cible aujourd'hui
        maintenant = datetime.now()
        heure_cible = maintenant.replace(hour=heure, minute=minute, second=0, microsecond=0)
        print(heure_cible)

        # Si l'heure est déjà passée, programmer pour demain
        if heure_cible <= maintenant:
            heure_cible += timedelta(days=1)
            self.afficher_message(f"⏰ Heure passée, programmé pour demain {heure:02d}h{minute:02d}") # pyright: ignore[reportAttributeAccessIssue]

        # Calculer le délai en secondes
        delai = (heure_cible - maintenant).total_seconds()

        # Attendre le délai
        time.sleep(delai)

        # Envoyer le message
        try:

            envoyer_whatsapp()
            self.afficher_message("✅ Message programmé envoyé !") # pyright: ignore[reportAttributeAccessIssue]
            self.fenetre.after(2000, self.retour_menu) # pyright: ignore[reportAttributeAccessIssue]
        except Exception as e:
            self.afficher_message(f"❌ Erreur envoi : {e}") # pyright: ignore[reportAttributeAccessIssue]

    def non_envoi(self):
        self.afficher_message("D'accord on va s'en passer 😒")     # pyright: ignore[reportAttributeAccessIssue]
        self.fenetre.after(2000, self.retour_menu) # pyright: ignore[reportAttributeAccessIssue]

    def retour_menu(self):
        # Nettoyer tous les boutons actuels
        for widget in self.frame_boutons.winfo_children(): # pyright: ignore[reportAttributeAccessIssue]
            widget.destroy()

        # Afficher message de transition
        self.afficher_message("\n🔄 Retour au menu principal...\n") # pyright: ignore[reportAttributeAccessIssue]

        # Recréer le menu principal
        self.menu_principal()  # type: ignore

    def envoie_message(self):
        self.afficher_message('Veux-tu envoyer le message du jour?') # pyright: ignore[reportAttributeAccessIssue]

        btn_oui = Button(
            self.frame_boutons, # pyright: ignore[reportAttributeAccessIssue]
            text="😊 Oui",
            command=lambda: self.envoie()
        )
        btn_non = Button(
            self.frame_boutons, # pyright: ignore[reportAttributeAccessIssue]
            text="😟 non",
            command=lambda: self.non_envoi()
        )
        btn_oui.pack(side="left", padx=10)
        btn_non.pack(side="left", padx=10)
