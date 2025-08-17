import subprocess
import time


def choice_3():

    subprocess.run(["open", "/Applications/Visual Studio Code.app"])


def choice_2():
    subprocess.run(["open", "/Applications/GeForceNOW.app"])


def choice_1():

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


def treatement_choice_app(choice_app):
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
