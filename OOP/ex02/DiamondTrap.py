#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Classe pour representer le Roi."""

    def __init__(self, name: str, alive = True,
                 family_name = 'Baratheon',
                 eyes = 'brown',
                 hairs = 'dark'):
        """Methode Constructeur du Roi."""

        Baratheon.__init__(self, name, alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs =  hairs


    def get_eyes(self) -> str:
        """Renvoie la couleur des yeux du Roi."""
        return (self.eyes)
    

    def get_hairs(self) -> str:
        """Renvoie la couleur des cheveux du Roi."""
        return (self.hairs)
    

    def set_eyes(self, eyes: str) -> None:
        """Change la couleurs des yeux du Roi."""
        self.eyes = eyes


    def set_hairs(self, hairs: str) -> None:
        """Change la couleurs des cheveux du Roi."""
        self.hairs = hairs