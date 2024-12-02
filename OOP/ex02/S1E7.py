#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################
from S1E9 import Character

class Baratheon(Character):
    """Classe pour representer la fammile Baratheon."""

    def __init__(self, name: str, alive = True,
                 family_name = 'Baratheon',
                 eyes = 'brown',
                 hairs = 'dark'):
        """Methode Constructeur Baratheon."""

        Character.__init__(self, name, alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs =  hairs


    def __str__(self):
        """méthode spéciale __str__ permet d'indiquer la représentation
        en chaîne de caractères d'un objet."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


    def __repr__(self):
        """méthode spéciale __repr__ permet d'indiquer la représentation
        en chaîne de caractères d'un objet.
        Sa représentation permet généralement de recréer l'objet en question."""
        
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        
    
# ----------------------------------------------------------------- #
class Lannister(Character):
    """Classe pour representer la fammile Lannister."""

    def __init__(self, name: str, alive = True,
                 family_name = 'Lannister',
                 eyes = 'blue',
                 hairs = 'light'):
        """Methode Constructeur Lannister."""

        Character.__init__(self, name, alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs =  hairs


    def __str__(self):
        """méthode spéciale __str__ permet d'indiquer la représentation
        en chaîne de caractères d'un objet."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


    def __repr__(self):
        """méthode spéciale __repr__ permet d'indiquer la représentation
        en chaîne de caractères d'un objet.
        Sa représentation permet généralement de recréer l'objet en question."""
        
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        

    def create_lannister(name: str, alive = True):
        """Methode creation Classe enfant Lannister"""

        return (Lannister(name, alive))
