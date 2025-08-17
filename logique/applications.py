import subprocess

def choice_3():
    """
    Ouvre Visual Studio Code

    Raises:
        FileNotFoundError: Si Visual Studio Code n'est pas installé au chemin spécifié
    """
    subprocess.run(["open", "/Applications/Visual Studio Code.app"])


def choice_2():
    """
    Ouvre l'application GeForce Now
    Raises:
        FileNotFoundError: Si GeForce Now n'est pas installé au chemin spécifié
    """
    subprocess.run(["open", "/Applications/GeForceNOW.app"])


def choice_1():
    """
    Ouvre le site de la banque et le site notion avec le profil 1 de chrome

    Raises:
        FileNotFoundError: Si Chrome n'est pas installé au chemin spécifié
    """
    subprocess.Popen(
        [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--profile-directory=Profile 1",
            "https://www.notion.so/D-penses-c83096354dfa422ba0d229a03693d676",
            "https://www.caisse-epargne.fr/bourgogne-franche-comte/",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def treatment_choice_app(choice_app):
    """
    Suite au choix de l'utilisateur, ouvre l'application ou les sites demandés

    Args :
        choice_app[str]: utilisateur invité à entrer
            '1' -> faire les comptes -> ouverture de page web
            '2' -> jouer -> ouverture de GeForce Now
            '3' -> coder -> ouverture de vs code

    Returns :
        str: Message humouristique validant l'action lancée. Exemple : "J'espère que cela ne sera pas douloureux 😅"

    """
    if choice_app == "1":
        choice_1()
        return "J'espère que cela ne sera pas douloureux 😅"
    elif choice_app == "2":
        choice_2()
        return "un peu de détente ça fait plaisir 🕹️"
    elif choice_app == "3":
        choice_3()
        return "Rappelle toi que tu es doué"
    else:
        return "On peut ne rien faire aussi en effet 🤣"
