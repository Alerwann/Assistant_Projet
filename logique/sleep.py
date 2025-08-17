def treat_resp_sleep(resp_sleep):
    """
    Retourne une réponse suite à la qualité de sommeil de l'utilisateur.

    Args:
        resp_sleep (str): Réponse de l'utilisateur ('y' pour oui, 'n' pour non)

    Returns:
        str: Message d'encouragement basé sur la réponse

    Example:
        >>> treat_resp_sleep("y")
        "🥳 ça va être une excellente journée"
    """

    if resp_sleep == "y":
        return "🥳 ça va être une excellente journée"
    elif resp_sleep == "n":
        return "🥲 On va tout faire pour que ta journée soit bonne"
    else:
        return "😡Tu cherches à me contredire 🤣"
