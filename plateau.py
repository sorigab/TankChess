"""TankChess

Grille du jeu
"""


class Cellule:
    """
    La classe représente une case de la grille de jeu.
    Chaque case de jeu dispose d’une coordonnée et d’une marque.
    La marque représente ce qui se trouve sur la case
    """

    def __init__(self, longitude, latitude, mark="~"):
        self.longitude = longitude
        self.latitude = latitude
        self.mark = mark

    def __str__(self):
        return self.mark

    def __repr__(self):
        return f"<Cellule ({self.longitude}, {self.latitude}: {self.mark})>"

    def get_coordonnee(self):
        """Retourne la coordonnée de la case"""
        return (self.longitude, self.latitude)

    def get_mark(self):
        """Retourne la marque de la case"""
        return self.mark

    def __set_mark(self, mark):
        """Modifie la marque de la case"""
        self.mark = mark

    def set_empty(self):
        """modifie la marque de la case en ("~")"""
        self.__set_mark("~")

    def set_destroyed(self):
        """modifie la marque de la case en ("X")"""
        self.__set_mark("X")

    def set_occuped(self):
        """modifie la marque de la case en ("O")"""
        self.__set_mark("O")

class Grille:
    """
    La classe représente une grille de jeu.
    """

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.carte: dict[str, Cellule] = {}
        for i in range(self.largeur):
            for j in range(self.longueur):
                self.carte[str(j) + str(i + 1)] = Cellule(j, i)

    def get_grille(self):
        """Retourne la grille de jeu"""
        return self.carte

    def afficher(self):
        """Affiche la grille de jeu"""
        for i in range(self.largeur):
            for j in range(self.longueur):
                print(self.carte[str(j) + str(i + 1)], end=" ")
            print()


if __name__ == "__main__":
    grille = Grille(10, 10)
    grille.afficher()
