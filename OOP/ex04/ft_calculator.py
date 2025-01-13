#####################################################################
# Classe Python ft_calculator                                       #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################

#####################################################################
# Definition des Classes :
class calculator:
    """Classe calculatrice permettent d'effectuer des calculs sur
    un vecteur avec un scalaire."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Calcule le produit point de deux vecteurs.
        :param V1 : Premier vecteur
        :param V2 : Deuxième vecteur"""
        produit = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is: ", produit)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calcule l'addition de deux vecteurs.
        :param V1 : Premier vecteur
        :param V2 : Deuxième vecteur"""
        somme = [float(x) + float(y) for x, y in zip(V1, V2)]
        print("Add Vector is :", somme)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calcule la soustraction de deux vecteurs.
        :param V1 : Premier vecteur
        :param V2 : Deuxième vecteur"""
        resultat = [float(x) - float(y) for x, y in zip(V1, V2)]
        print("Sous Vector is :", resultat)
