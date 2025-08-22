import time
import threading
import subprocess
import sys
import os


def get_bundled_terminal_notifier():
    """Retourne le chemin vers terminal-notifier bundlé"""
    if getattr(sys, "frozen", False):
        # L'application est "frozen" (compilée avec PyInstaller)
        base_path = sys._MEIPASS
        notifier_path = os.path.join(base_path, "terminal-notifier")
    else:
        # Mode développement - cherche dans le dossier parent
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)  # Remonte d'un niveau
        notifier_path = os.path.join(project_root, "assets", "terminal-notifier")
        print(f"Script dir: {script_dir}")
        print(f"Project root: {project_root}")
        print(f"Cherche dans: {notifier_path}")

    return notifier_path


def send_breakfast_notification():
    """
    Envoie de notification quand timer fini après un délais de 5s
    Utilise terminal-notifier pour afficher une notification système
    indiquant que le temps de petit-déjeuner est arrivé.
    """
    print("=== DEBUT send_breakfast_notification ===")

    notifier_path = get_bundled_terminal_notifier()

    if not os.path.exists(notifier_path):
        print("ERREUR: terminal-notifier non trouvé !")
        print("Tentative avec terminal-notifier du système...")
        notifier_path = "terminal-notifier"  # Fallback vers le PATH système

    try:
        print(f"Tentative d'exécution avec: {notifier_path}")

        result = subprocess.run(
            [
                notifier_path,
                "-title",
                "Assistant",
                "-message",
                "Tu peux prendre ton petit déjeuner",
                "-subtitle",
                "Bon appétit 🤤",
                "-sound",
                "default",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )

        print(f"Code de retour: {result.returncode}")
        print(f"Stdout: '{result.stdout}'")
        print(f"Stderr: '{result.stderr}'")

        if result.returncode == 0:
            print("✅ Notification envoyée avec succès!")
        else:
            print("❌ Échec de l'envoi de notification")

    except subprocess.TimeoutExpired:
        print("❌ TIMEOUT: terminal-notifier a pris trop de temps")
    except FileNotFoundError as e:
        print(f"❌ ERREUR: Fichier non trouvé - {e}")
    except Exception as e:
        print(f"❌ ERREUR inattendue: {e}")

    print("=== FIN send_breakfast_notification ===")


def send_timer(duration, type):
    """Lance le timer en arrière-plan"""
    print(f"Lancement timer: {duration}s, type: {type}")
    threading.Thread(
        target=lambda: general_timer(duration=duration, type=type), daemon=False
    ).start()


def general_timer(duration, type):
    """Timer interne avant notification notification"""
    print(f"Timer démarré: {duration}s")
    time.sleep(int(duration))
    print(f"Timer fini, type: {type}")

    if type == "breakfast":
        send_breakfast_notification()
    elif type == "whatsapp":
        send_whatsappenvoie_notification()
    else:
        error_timer()


def send_whatsappenvoie_notification():
    """
    Envoie de notification WhatsApp
    """
    print("=== DEBUT send_whatsappenvoie_notification ===")

    notifier_path = get_bundled_terminal_notifier()

    if not os.path.exists(notifier_path):
        print("ERREUR: terminal-notifier non trouvé !")
        notifier_path = "terminal-notifier"

    try:
        result = subprocess.run(
            [
                notifier_path,
                "-title",
                "Assistant",
                "-message",
                "Attention je vais ouvrir Whatsapp dans quelque secondes",
                "-subtitle",
                "NE TOUCHE À RIEN",
                "-sound",
                "default",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )

        print(f"Code de retour WhatsApp: {result.returncode}")
        if result.stderr:
            print(f"Stderr WhatsApp: {result.stderr}")

    except Exception as e:
        print(f"Erreur WhatsApp notification: {e}")

    print("=== FIN send_whatsappenvoie_notification ===")


def error_timer():
    """
    Notification d'erreur
    """
    print("=== DEBUT error_timer ===")
    time.sleep(5)

    notifier_path = get_bundled_terminal_notifier()

    if not os.path.exists(notifier_path):
        notifier_path = "terminal-notifier"

    try:
        subprocess.run(
            [
                notifier_path,
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
    except Exception as e:
        print(f"Erreur error_timer: {e}")

    print("=== FIN error_timer ===")


# Test direct pour debug
if __name__ == "__main__":
    print("=== TEST DE DEBUG ===")
    send_breakfast_notification()
