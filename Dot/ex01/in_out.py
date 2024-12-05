#####################################################################
# Fonctions Python : Outer_inner [Module Dot]                        #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################


def square(x: int | float) -> int | float:
    """
    Fonction qui renvoie le carré de l'argument.
    """

    # Verifie l'argument :
    if not isinstance(x, (int, float)):
        print("Erreur : l'argument doit etre un int ou un float.")
        return
    
    return (x * x)

# ----------------------------------------------------------------- #
def pow(x: int | float) -> int | float:
    """
    Fonction qui renvoie l'exponentiation de l'argument par lui-même.
    """
    
    # Verifie l'argument :
    if not isinstance(x, (int, float)):
        print("Erreur : l'argument doit etre un int ou un float.")
        return
    
    return (x **x)

# ----------------------------------------------------------------- #
def outer(x: int | float, function) -> object:
    """
    Fonction qui prend comme argument un nombre et renvoie un objet.
    """
    
    count = 0
    # Verifie l'argument :
    if not isinstance(x, (int, float)):
        print("Erreur : le 1er argument doit etre un int ou un float.")
        exit(1)

    def inner() -> float:
        # nonlocal permet de modifier notre variable 'x' :
        nonlocal x
        result = function(x)
        # Stocke le resulat precedent :
        x = result
        return (result)

    # On retourne la fonction inner comme un objet
    return inner
    