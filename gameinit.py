"""import modules des modules du jeu + initialise les objets du jeu"""

import plateau

def gameinit():
    """Initialise"""

    carte = plateau.Grille(10, 10)

    return carte


if __name__ == "__main__":
    gameinit()
    # plateau.Grille(10, 10).afficher()
