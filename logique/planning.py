import csv
import datetime as dt
import locale
import subprocess

from config import CONVERSATION_NAME, CSV_PATH

# Configurer en français
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


def download_planning_csv():
    """
    Importe le fichier cvs du planning de la semaine

    Utilise CSV pour le traitement du fichier et convertir chaque ligne en dict

    Returns:
        list[Dict|str,str]] contenant les infos de chaque jour: Menu du midi, Menu du soir, Rendez-vous, Crème du soir, Mot doux

    Raises:
        FileNotFoundError: Si le fichier CSV n'existe pas
    """
    planning = []
    with open(
        CSV_PATH, newline="", encoding="utf-8"
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            planning.append(dict(row))  # Convertir en dict normal
    return planning


def get_daily_information(day_name):
    """
    Récupère les informations de planning pour un jour donné.

     Args:
         day_name (str): Nom du jour de la semaine (ex: "lundi")

     Returns :
        
         Dict[str, str]: Dictionnaire contenant les infos du jour
         ou dictionnaire vide si pas trouvé
    """
    planning = download_planning_csv()
    for jour in planning:
        if jour["Jour"].lower() == day_name.lower():
            return jour
    return {}


def create_daily_message():
    """
        A partir des informations du jour, crée le message à envoyer.

        Returns:
           list[str,str,str,str,str] ex: ["lundi","pates","soupe","12h medecin","jaune","je t'aime"]
    """
    current_day = dt.date.today().strftime("%A").lower()

    daily_planning = get_daily_information(current_day)

    midi = daily_planning.get("Menu du midi", "").strip() or "Pas de repas à midi"
    evening = daily_planning.get("Menu du soir", "").strip() or "Pas de repas prévu"
    meeting = daily_planning.get("Rendez-vous", "").strip() or "Pas de rdv"
    cream = daily_planning.get("Crème du soir", "").strip() or "Demande moi au cas où"
    love_message = (daily_planning.get("Message doux", "").strip() or "Je t'aime "
    )
    messsage = [current_day, midi, evening, meeting, cream, love_message]
   
    return messsage


def must_send_message(response_send):
    """
    Choix si l'utilisateur veut envoyer le message quotidien

    Args:
        response_send (str): Réponse de l'utilisateur ('y' pour oui, 'n' pour non)

    Return:
        str: Message demandant quand envoyer si 'y', ou message de refus
            si 'n'. Exemple: "D'accord on va s'en passer 😒"
    """
    if response_send == "y":

        return "Maintenant ou plus tard? ⏰"
    else:

        return "D'accord on va s'en passer 😒"


def send_whatsapp():
    """
    Envoie un message WhatsApp automatisé avec le planning du jour.

    Utilise AppleScript pour automatiser l'envoi d'un message 

    Returns:
        bool: True si envoi réussi, False sinon

    Raises:
        subprocess.CalledProcessError: Si l'exécution AppleScript échoue

    Note:
        Nécessite que WhatsApp soit installé sur macOS
    """
    message = create_daily_message()

    script_applescript = f"""

   
    -- Force kill seulement si encore vivant
        try
            do shell script "pgrep -f WhatsApp"
            do shell script "pkill -f WhatsApp"
        end try
        delay 2
  
    
    -- Relancer WhatsApp (état propre)
    tell application "WhatsApp"
        activate
        delay 15  -- Plus de temps pour le lancement
    end tell
    
   
    tell application "System Events"
        tell process "WhatsApp"
            -- Raccourci clavier pour chercher (Cmd+F)
            key code 3 using command down
            delay 5

                       
            -- Taper le nom du contact
            keystroke "{CONVERSATION_NAME}"
            delay 3

            -- 2 fois flèche bas
            key code 125  -- Flèche bas
            delay 1
            key code 125  -- Flèche bas encore
            delay 1
            
           -- appuyer sur entré
           key code 36
           delay 1
                                  
            -- Taper le message ligne par ligne
            
           keystroke "Coucou bébé"
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "On est {message[0]}. "
           delay 0.3
           keystroke ":coeur"
           delay 1
           key code 36 --entrée
           delay 0.3
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "A midi on mange : {message[1]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée 
           delay 0.3
           keystroke "Ce soir on mange : {message[2]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Les événements importants : {message[3]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Ce soir tu mets la crème : {message[4]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Et surtout tu n'oublies pas: {message[5]}. "
           keystroke ":amour"
           delay 1
           key code 36 --entrée
           delay 0.3
            
         
            
            -- Envoyer (Entrée)
            key code 36
        end tell
    end tell

     """
    script_debug = """
    tell application "WhatsApp"
        activate
    end tell

    tell application "System Events"
        tell process "WhatsApp"
        return entire contents
    end tell
    end tell
    """
    try:
        subprocess.run(["osascript", "-e", script_applescript], check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def must_send_message_cli(reponse):
    """
    Action effectué suivant le choix d'envoie du message

    Args:
        str: "y" pour oui "n" pour non

    Returns:
        pour 'y' envoie le message et retoune str pour valider
        pour 'n' ou autre texte : str
        exemple: "On va faire sans 😒"
    """

    if reponse == "y":
        send_whatsapp()
        return "C'est envoyé"

    elif reponse == "n":
        return "On va faire sans 😒"

    else:
        return "J'ai compris tu veux pas répondre à mes choice🤣"
