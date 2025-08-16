import time
import threading

import subprocess


def envoyer_notifiaction_petit_dej():
    time.sleep(5)
    subprocess.run(
        [
            "terminal-notifier",
            "-title",
            "Assistant",
            "-message",
            "Tu peux prendre ton petit déjener",
            "-subtitle",
            "Bonne appétit 🤤",
            "-sound",
            "default",
        ]
    )


def lancer_timer_30min():
    """Lance le timer de 30min en arrière-plan"""
    threading.Thread(target=_timer_petit_dej, daemon=False).start()


def _timer_petit_dej():
    """Timer interne de 30min puis notification"""
    time.sleep(30 * 60)  # 30 minutes
    envoyer_notifiaction_petit_dej()
