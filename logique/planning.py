import csv
import datetime as dt
import locale
from datetime import datetime, timedelta
import subprocess


# Configurer en français
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


def donwload_planning_cvs():
    planning = []
    with open(
        "/Users/alerwann/Desktop/menu.csv", newline="", encoding="utf-8"
    ) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            planning.append(dict(row))  # Convertir en dict normal
    return planning


def get_daily_information(jour_nom):
    planning = donwload_planning_cvs()
    for jour in planning:
        if jour["Jour"].lower() == jour_nom.lower():
            return jour
    return {}


def create_daily_message():
    daily_date = dt.date.today().strftime("%A").lower()

    daily_planning = get_daily_information(daily_date)

    midi = daily_planning.get("Menu du midi", "").strip() or "Pas de repas à midi"
    night = daily_planning.get("Menu du night", "").strip() or "Pas de repas prévu"
    meeting = daily_planning.get("Rendez-vous", "").strip() or "Pas de rdv"
    creame = daily_planning.get("Crème du night", "").strip() or "Demande moi au cas où"
    love_message = (
        daily_planning.get("Message doux", "").strip() or "Je t'aime mon bébé d'amour"
    )
    messsage = [daily_date, midi, night, meeting, creame, love_message]
    # message=f"Coucou Bébé ❤️ \n C'est {daily_date} aujourd'hui. À midi on manges : {midi}. Ce night tu auras : {night}. \n Les choses importantes pour aujourd'hui: {meeting}.\n Ce night ce sera la crème {creame} pour ton torse.\n Et surtout n'oublie pas : {love_message}"
    return messsage


def must_send_message(response_send):
    if response_send == "y":

        return "Maintenant ou plus tard? ⏰"
    else:

        return "D'accord on va s'en passer 😒"


def horaire_choice(response_heure):
    if response_heure == "maintenant":
        heure = datetime.now()
    else:
        heure = response_heure
    return heure


def send_whatsapp():
    message = create_daily_message()

    nom_du_contact = "marie guehl"

    script_applescript = f"""

    -- Vérifier si WhatsApp tourne
    if application "WhatsApp" is running then
        tell application "WhatsApp" to quit
        delay 2
    
    -- Force kill seulement si encore vivant
        try
            do shell script "pgrep -f WhatsApp"
            do shell script "pkill -f WhatsApp"
        end try
        delay 2
    end if
    
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
            keystroke "{nom_du_contact}"
            delay 3

            -- 2 fois flèche bas
            key code 125  -- Flèche bas
            delay 0.3
            key code 125  -- Flèche bas encore
            delay 0.3
            
           -- appuyer sur entré
           key code 36
           delay 0.3
                                  
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
           keystroke "Ce night on mange : {message[2]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Les événements importants : {message[3]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Ce night tu mets la crème : {message[4]}."
           delay 1
           key code 36 using shift down  -- Shift+Entrée
           delay 0.3
           keystroke "Et surtout tu n'oublies pas: {message[5]}. "
           keystroke ":bisou"
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

    if reponse == "y":
        send_whatsapp()
        return "C'est envoyé"

    elif reponse == "n":
        return "On va faire sans 😒"

    else:
        return "J'ai compris tu veux pas répondre à mes choice🤣"
