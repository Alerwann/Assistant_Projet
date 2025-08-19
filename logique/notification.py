import time
import threading

import subprocess


def send_breakfast_notification():
    """
    Envoie de notification quand timer fini après un délais de 5s
    Utilise terminal-notifier pour afficher une notification système
    indiquant que le temps de petit-déjeuner est arrivé.

    Note:
        Utilise terminal-notifier

    Raises:
        FileNotFoundError: Si terminal-notifier n'est pas installé
    """
    # time.sleep(5)
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            "Assistant",
            "-message",
            "Tu peux prendre ton petit déjeuner",
            "-subtitle",
            "Bon appétit 🤤",
            "-sound",
            "default",
        ]
    )


def send_timer(duration, type):
    """Lance le timer en arrière-plan"""
 
    threading.Thread(target=lambda: general_timer(duration = duration,type=type), daemon=False).start()


def general_timer(duration,type):
    """Timer interne avant notification notification"""
    print(duration)
    time.sleep(int(duration))  
    if type == 'breakfast':
        send_breakfast_notification()
    elif type == 'whatsapp':
        send_whatsappenvoie_notification()
    else: return error_timer()


def send_whatsappenvoie_notification():
    """
    Envoie de notification quand timer fini après un délais de 5s
    Utilise terminal-notifier pour afficher une notification système
    indiquant que le temps de petit-déjeuner est arrivé.

    Note:
        Utilise terminal-notifier

    Raises:
        FileNotFoundError: Si terminal-notifier n'est pas installé
    """
    # time.sleep(5)
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            "Assistant",
            "-message",
            "Attention je vais ouvrir Whatsapp dans quelque secondes",
            "-subtitle",
            "NE TOUCHE À RIEN",
            "-sound",
            "default",
        ]
    )

def error_timer():
    time.sleep(5)
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            "Assistant",
            "-message",
            "Error mon grand",
            "-subtitle",
            "timer de 5s, tu as mal définit la commande",
            "-sound",
            "default",
        ]
    )
