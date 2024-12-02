#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################

def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    - Args: les arguments passes en parametre sont paquetes dans args qui 
    se comporte comme un tuple.
    - Kwargs: les arguments passes en parametre sont paquetes dans kwargs qui
    se comporte comme un dictionnaire.
    """

    for value in kwargs.values():
        if len(args) == 0:
            print("ERROR")
        elif value == 'mean':
            mean = (sum(x for x in args) / len(args))
            print("mean :", mean)
        elif value == 'median':
            sorted_args = sorted(args)
            if len(args) % 2 == 0:
                milieu = len(args) / 2
                median = (sorted_args[int(milieu)] + sorted_args[int(milieu - 1)]) /2
            else:
                median = sorted_args[int(len(args) / 2)]
            print("median :", median)
        elif value == 'quartile':
            print("quartile :")
        elif value == 'std':
            print("std :")
        elif value == 'var':
            print("var :")

