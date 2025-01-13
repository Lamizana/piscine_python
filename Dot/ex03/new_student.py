#####################################################################
# Fonction Python : Data class [Module Dot]                         #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
import random
import string
from dataclasses import dataclass, field


#####################################################################
# Definition de fonctions :
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


# ----------------------------------------------------------------- #
@dataclass
class Student:
    """
    Classe student.
    @dataClasse est un décorateur qui ajoute aux classes
    des méthodes spéciales générées automatiquement.
    """

    name: str = "John"
    surname: str = "Doe"
    active: bool = True
    login: str = field(init=False, default="Eagle")
    id: str = field(init=False, default=generate_id())
