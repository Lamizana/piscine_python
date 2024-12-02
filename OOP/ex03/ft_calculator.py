#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################

class calculator(object):
    """Classe calculatrice permettent d'effectuer des calculs sur
    un vecteur avec un scalaire."""

    def __init__(self, vector):
        """Initialise la calculatrice avec un vecteur.
        :param vector: liste ou tuple de nombres représentant le vecteur"""
        self.vector = list(vector)


    def __add__(self, object) -> None:
        """Methode addition à chaque élément du vecteur."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)


    def __mul__(self, object) -> None:
        """Methode multiplication à chaque élément du vecteur."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)


    def __sub__(self, object) -> None:
        """Methode soustraction à chaque élément du vecteur."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)


    def __truediv__(self, object) -> None:
        """Methode division à chaque élément du vecteur."""
        if object == 0:
            print("Division par 0 impossible.")
        else:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
