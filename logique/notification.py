import time
import threading

import subprocess


def send_breakfast_notification():
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


def send_30min_timer():
    """Lance le timer de 30min en arrière-plan"""
    threading.Thread(target=breakfast_timer, daemon=False).start()


def breakfast_timer():
    """Timer interne de 30min puis notification"""
    time.sleep(30 * 60)  # 30 minutes
    send_breakfast_notification()
