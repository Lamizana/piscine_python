#####################################################################
# Fonctions Python : Outer_inner [Module Dot]                        #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################

def isValid(x: int | float) -> bool:
    """Verifie si la valeur est un int ou un float."""

    if not isinstance(x, (int, float)):
        print("Erreur : l'argument doit etre un int ou un float.")
        return (False)
    return (True)


# ----------------------------------------------------------------- #
def square(x: int | float) -> int | float:
    """Fonction qui renvoie le carré de l'argument."""

    if isValid(x) is False:
        return
    return (x * x)


# ----------------------------------------------------------------- #
def pow(x: int | float) -> int | float:
    """Fonction qui renvoie l'exponentiation de l'argument par lui-même."""

    if isValid(x) is False:
        return
    return (x ** x)


# ----------------------------------------------------------------- #
def outer(x: int | float, function) -> object:
    """Fonction qui prend comme argument un nombre et renvoie un objet."""

    count = 0
    if isValid(x) is False:
        exit(1)

    def inner() -> float:
        # nonlocal permet de modifier notre variable 'count' :
        nonlocal count
        result = function(x)
        for i in range(count):
            result = function(result)
        count += 1

        return (result)

    # On retourne la fonction inner comme un objet
    return inner
