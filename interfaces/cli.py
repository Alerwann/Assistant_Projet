import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logique.sleep import treat_resp_sleep
from logique.notification import send_30min_timer
from logique.planning import must_send_message_cli
from logique.applications import treatment_choice_app


def assistant_cli():
    print("Salut je suis ton assistant préféré")
    sleep_choice = input("Tu as bien dormi? y/n \n")
    sleep_result = treat_resp_sleep(sleep_choice)
    print(sleep_result, "\n")

    send_30min_timer()
    print("j'au lancé le timer pour savoir quand tu pourras déjeuner!🤤 \n")

    message_choice = input("Veux tu envoyer message du jour? y/n \n")
    print(must_send_message_cli(message_choice), "\n")

    print("Passons aux choses sérieuses")
    print("Quelle application veux tu lancer ?\n")
    app_choice = input(
        "Choix 1: La gestion des comptes \n"
        "Choix 2 : Jouer\n"
        "Choix 3 : Faire du code \n"
    )
    print(treatment_choice_app(app_choice))


assistant_cli()
