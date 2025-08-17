import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logique.sommeil import traiter_reponse_sommeil
from logique.notification import lancer_timer_30min
from logique.planning import doit_envoyer_message_cli
from logique.applications import traitement_choix_app


def assistant_cly():
    print("Salut je suis ton assistant préféré")
    choix_dormir=input("Tu as bien dormi? y/n \n")
    result_sommeil=traiter_reponse_sommeil(choix_dormir)
    print(result_sommeil,"\n")
    
    lancer_timer_30min()
    print("j'au lancé le timer pour savoir quand tu pourras déjeuner!🤤 \n" )
  
    choix_message = input("Veux tu envoyer le message du jour? y/n \n")
    print(doit_envoyer_message_cli(choix_message),"\n")

    print("Passons aux choses sérieuses")
    print("Quelle application veux tu lancer ?\n")
    choix_app =input("Choix 1: La gestion des comptes \nChoix 2 : Jouer\nChoix 3 : Faire du code \n")
    print(traitement_choix_app(choix_app))
    
    
    

assistant_cly()
