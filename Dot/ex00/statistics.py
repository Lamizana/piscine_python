#####################################################################
# Fonction Python Calculate my statistics                           #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################


#####################################################################
# Definition de fonctions :
def ft_quartile(data: tuple, quartile: int):
    """
    Fonction pour trouver le quartile.
    """

    lst = sorted(data)
    position = (len(lst) - 1) * quartile
    bas = int(position)
    haut = bas + 1
    poids = position - bas
    if haut < len(lst):
        return lst[bas] * (1 - poids) + lst[haut] * poids
    return lst[bas]

# ----------------------------------------------------------------- #
def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    - Args: les arguments passes en parametre sont paquetes dans args qui 
    se comporte comme un tuple.
    - Kwargs: les arguments passes en parametre sont paquetes dans kwargs qui
    se comporte comme un dictionnaire.
    """

    # Vérifie si tous les éléments sont des float ou int :
    isvalid = all(isinstance(x, (int, float)) for x in args)
    if isvalid is False:
        print("ERROR: List is not valid")
        return

    for value in kwargs.values():
        if len(args) == 0:
            print("ERROR")
        elif value == 'mean':
            print("mean :", sum(args) / len(args))
        elif value == 'median':
            print("median :", ft_quartile(args, .50))
        elif value == 'quartile':
            print(f"quartile : [{ft_quartile(args, .25)}, {ft_quartile(args, .75)}]")
        elif value == 'std':
            # La standard deviation (écart-type) est la racine carrée de la variance.
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print("std :",variance ** 0.5)
        elif value == 'var':
            # La variance mesure la dispersion d'un ensemble de données
            # par rapport à leur moyenne.
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print("var :", variance)
    return