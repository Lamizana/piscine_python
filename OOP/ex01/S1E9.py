#####################################################################
# Classes Python S1E9                                               #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from abc import ABC, abstractmethod


#######################################################################
# Definition des Classes :
class Character(ABC):
    """Classe abstraite Character avec un nom et un Booleen."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Constructeur classe abstraite Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Methode pour changer l'etat de sante a False."""
        self.is_alive = False


# ----------------------------------------------------------------- #
class Stark(Character):
    """Classe enfant de Character"""

    def __init__(self, first_name: str, is_alive=True):
        """Constructeur Stark"""
        Character.__init__(self, first_name, is_alive)
        self.first_name = first_name
        self.is_alive = is_alive
