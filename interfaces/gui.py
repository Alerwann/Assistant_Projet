# from tkinter import Tk, Label, Button, Text, Frame, Checkbutton, Entry, IntVar
# import sys
# import os
# import threading
# from tkinter import PhotoImage, ttk
# from datetime import timedelta,datetime
# import time

# # Ajouter le dossier parent au path pour importer logique
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from logique.sommeil import traiter_reponse_sommeil
# from logique.applications import choix_1, choix_2, choix_3
# from logique.notification import lancer_timer_30min
# from logique.planning import envoyer_whatsapp


# class AssistantGUI:
    # def __init__(self):
    #     self.fenetre = Tk()
    #     self.fenetre.title("🤖 Assistant Personnel")
    #     self.fenetre.geometry("600x500")

    #     # Zone d'affichage
    #     self.messages = Text(self.fenetre, height=20, width=70, font=("Arial", 13))
    #     self.messages.pack(pady=10)

    #     # Zone boutons
    #     self.frame_boutons = Frame(self.fenetre)
    #     self.frame_boutons.pack(pady=10)

    #     # Zone bouton à coché
    #     self.frame_check = Frame(self.fenetre)
    #     self.frame_check.pack(pady=10)

    #     # Zone de bouton quitter
    #     self.frame_quit_button =Frame(self.fenetre)
    #     self.frame_quit_button.pack(side="top", pady=10)

    #     self.btn_quitter_permanent = Button(
    #     self.frame_quit_button, 
    #     text="❌ Quitter", 
    #     command=self.quitter_complet,
    #     bg="lightcoral"  # Couleur pour le distinguer
    # )
    #     self.btn_quitter_permanent.pack()

    #     # Démarrer
    #     self.ecran_accueil()
    #     self.fenetre.mainloop()

    #     # Changemlent icon
    #     try:
    #         # Chemin vers l'icône depuis gui.py
    #         icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'icon_32.png')
    #         icon = PhotoImage(file=icon_path)
    #         self.fenetre.iconphoto(True, icon)
    #     except Exception as e:
    #         print(f"Impossible de charger l'icône : {e}")

    # def afficher_message(self, message):
    #     self.messages.insert("end", message + "\n")
    #     self.messages.see("end")

    # def ecran_accueil(self):
    #     self.afficher_message("👋 Salut Mon Maître")
    #     self.afficher_message("👀 Comment tu vas?")
    #     self.afficher_message("Tu as bien dormi? 🤔\n")

    #     # Boutons Y/N
    #     btn_oui = Button(
    #         self.frame_boutons,
    #         text="😊 Oui",
    #         command=lambda: self.repondre_sommeil("y"),
    #     )
    #     btn_non = Button(
    #         self.frame_boutons,
    #         text="😴 Non",
    #         command=lambda: self.repondre_sommeil("n"),
    #     )
        

    #     btn_oui.pack(side="left", padx=10)
    #     btn_non.pack(side="left", padx=10)
    # def repondre_sommeil(self, reponse):
    #     # Utiliser la logique séparée
    #     message = traiter_reponse_sommeil(reponse)
    #     self.afficher_message(message)

    #     # Nettoyer les boutons et passer au menu
    #     for widget in self.frame_boutons.winfo_children():
    #         widget.destroy()

    #     self.envoie_message()

    # def envoie_message(self):
    #     self.afficher_message('Veux-tu envoyer le message du jour?')

    #     btn_oui = Button(
    #         self.frame_boutons,
    #         text="😊 Oui",
    #         command=lambda: self.envoie()
    #     ) 
    #     btn_non = Button(
    #         self.frame_boutons,
    #         text="😟 non",
    #         command=lambda: self.non_envoi()
    #     )
    #     btn_oui.pack(side="left", padx=10)
    #     btn_non.pack(side="left", padx=10)

    # def menu_principal(self):
    #     self.afficher_message("\nPassons aux choses sérieuses, que veux-tu faire?\n")

    #     # Lancer le timer
    #     lancer_timer_30min()

    #     # Boutons d'action
    #     btn1 = Button(
    #         self.frame_boutons, text="📊 Comptes", command=self.action_comptes
    #     )
    #     btn2 = Button(self.frame_boutons, text="🎮 Jeu", command=self.action_jeu)
    #     btn3 = Button(self.frame_boutons, text="💻 Code", command=self.action_code)

    #     btn1.pack(side="left", padx=10)
    #     btn2.pack(side="left", padx=10)
    #     btn3.pack(side="left", padx=10)

    # def quitter_complet(self):
    #     """Arrête tout, y compris le timer"""
    #     self.afficher_message("Tu quittes la page et le timer va être annulé")
    #     os._exit(0)

    # def action_comptes(self):
    #     self.afficher_message("📊 Ouverture de tes comptes...")
    #     choix_1()

    # def action_jeu(self):
    #     self.afficher_message("🎮 Tu as raison, commençons en douceur!")
    #     choix_2()

    # def action_code(self):
    #     self.afficher_message("💻 Tu es d'humeur à te concentrer!")
    #     choix_3()


    # def envoie(self): 
    #     for widget in self.frame_boutons.winfo_children():
    #         widget.destroy()

    #     self.afficher_message("Très bien")
    #     self.afficher_message("Quand veux tu l'envoyer?")

    #     self.envoi_maintenant = IntVar()

    #     # Checkbox "Maintenant"
    #     btnCheck = Checkbutton(
    #     self.frame_boutons, 
    #     text="📤 Maintenant", 
    #     variable=self.envoi_maintenant,
    #     command=self.toggle_horaire  # Active/désactive les champs
    #     )
    #     btnCheck.pack(pady=10)

    #     # Frame pour les champs heure/minute
    #     self.frame_horaire = Frame(self.frame_boutons)
    #     self.frame_horaire.pack(pady=10)

    #     # Label + champ heure
    #     Label(self.frame_horaire, text="Ou programmer pour :").pack(side="left")

    #     self.heure_combo = ttk.Combobox(
    #     self.frame_horaire, 
    #     width=3,
    #     values=[f"{h:02d}" for h in range(24)],  # 00, 01, 02... 23
    #     state="readonly"  # Empêche la saisie manuelle
    #     )
    #     self.heure_combo.pack(side="left", padx=5)
    #     self.heure_combo.set("12")  # Valeur par défaut

    #     Label(self.frame_horaire, text="h").pack(side="left")

    #     # Menu déroulant minutes (0, 15, 30, 45 ou tous les 5 min)
    #     self.minute_combo = ttk.Combobox(
    #     self.frame_horaire,
    #     width=3,
    #     values=[f"{m:02d}" for m in range(0, 60, 15)],  # 00, 15, 30, 45
    #     # Ou pour toutes les 5 min : range(0, 60, 5)
    #     state="readonly"
    #     )
    #     self.minute_combo.pack(side="left", padx=5)
    #     self.minute_combo.set("00")  # Valeur par défaut

    #     # Bouton final
    #     btn_envoyer = Button(self.frame_boutons, text="✉️ Envoyer", command=self.executer_envoi)
    #     btn_envoyer.pack(pady=10)

    #     btn_quitter = Button(
    #         self.frame_quit_button, text="❌ Quitter", command=self.quitter_complet
    #     )
    #     btn_quitter.pack(side="left", padx=10)


    # def toggle_horaire(self):

    #     if self.envoi_maintenant.get():
    #         self.heure_combo.config(state="disabled")
    #         self.minute_combo.config(state="disabled")
    #     else:
    #         self.heure_combo.config(state="readonly")
    #         self.minute_combo.config(state="readonly")


    # def executer_envoi(self):
        
    #    if self.envoi_maintenant.get():
    #     # IMMÉDIATEMENT afficher le message d'attente
    #     self.afficher_message("⏳ Envoi en cours, veuillez patienter...")
        
    #     # Désactiver le bouton pour éviter les clics multiples
    #     for widget in self.frame_boutons.winfo_children():
    #         if isinstance(widget, Button):
    #             widget.config(state="disabled")
        
    #     # Forcer l'affichage immédiat
    #     self.fenetre.update()
        
    #     try:
    #         from logique.planning import envoyer_whatsapp
    #         envoyer_whatsapp()
    #         self.afficher_message("✅ Message envoyé avec succès !")
    #     except Exception as e:
    #         self.afficher_message(f"❌ Erreur : {e}")
        
    #     # Retour menu après 2 secondes
    #         self.fenetre.after(2000, self.retour_menu)

    #     else:
    #         heure = int(self.heure_combo.get())
    #         minute = int(self.minute_combo.get())

    #         self.afficher_message(f"⏰ Message programmé pour {heure:02d}h{minute:02d}")
    #         self.programmer_envoi(heure, minute)

    #     self.afficher_message("✅ Message programmé envoyé !")
    #     self.fenetre.after(2000, self.retour_menu) 



    # def programmer_envoi(self, heure, minute):
    #     # Timer en thread séparé
    #     threading.Thread(target=self._envoi_differe, args=(heure, minute), daemon=True).start()

    # def _envoi_differe(self, heure, minute):
    #     # Calculer l'heure cible aujourd'hui
    #     maintenant = datetime.now()
    #     heure_cible = maintenant.replace(hour=heure, minute=minute, second=0, microsecond=0)
    #     print(heure_cible)

    #     # Si l'heure est déjà passée, programmer pour demain
    #     if heure_cible <= maintenant:
    #         heure_cible += timedelta(days=1)
    #         self.afficher_message(f"⏰ Heure passée, programmé pour demain {heure:02d}h{minute:02d}")

    #     # Calculer le délai en secondes
    #     delai = (heure_cible - maintenant).total_seconds()

    #     # Attendre le délai
    #     time.sleep(delai)

    #     # Envoyer le message
    #     try:

    #         envoyer_whatsapp()
    #         self.afficher_message("✅ Message programmé envoyé !")
    #         self.fenetre.after(2000, self.retour_menu)
    #     except Exception as e:
    #         self.afficher_message(f"❌ Erreur envoi : {e}")

    # def non_envoi(self):
    #     self.afficher_message("D'accord on va s'en passer 😒")    
    #     self.fenetre.after(2000, self.retour_menu)



    # def retour_menu (self):
        # Nettoyer tous les boutons actuels
        for widget in self.frame_boutons.winfo_children():
            widget.destroy()

        # Afficher message de transition
        self.afficher_message("\n🔄 Retour au menu principal...\n")

        # Recréer le menu principal
        self.menu_principal() # type: ignore

# if __name__ == "__main__":
#     AssistantGUI()
