#####################################################################
# Programme Python statistics                                       #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from statistics import ft_statistics


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")

    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")

    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")

    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

    return (0)


#####################################################################
if __name__ == "__main__":
    main()
