#####################################################################
# Programme Python ft_calculator                                    #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from ft_calculator import Calculator


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    v1 = Calculator([0.0, 1, 2.0, 3.0, 4.0, 5.0])
    v1 + 5

    print("---")
    v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5

    print("---")
    v3 = Calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    return (0)


#####################################################################
if __name__ == "__main__":
    main()
