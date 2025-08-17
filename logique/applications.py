import subprocess
import time


def choix_3():
 
    subprocess.run(["open", "/Applications/Visual Studio Code.app"])


def choix_2():
    subprocess.run(["open", "/Applications/GeForceNOW.app"])


def choix_1():

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


def traitement_choix_app (choix_app):
    if choix_app =='1':
        choix_1()
        return "J'espère que cela ne sera pas douloureux 😅"
    elif choix_app=='2':
        choix_2()
        return "un peu de détente ça fait plaisir 🕹️"
    elif choix_app=='3':
        choix_3()
        return "Rappelle toi que tu es doué"
    else :return "On peut ne rien faire aussi en effet 🤣"
