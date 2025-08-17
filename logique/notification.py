import time
import threading

import subprocess
from config import BREAKFAST_TIMER_MINUTES

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
    time.sleep(5)
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


def send_30min_timer():
    """Lance le timer de 30min en arrière-plan"""
    threading.Thread(target=breakfast_timer, daemon=False).start()


def breakfast_timer():
    """Timer interne de 30min puis notification"""
    time.sleep(BREAKFAST_TIMER_MINUTES * 60)  # 30 minutes
    send_breakfast_notification()
