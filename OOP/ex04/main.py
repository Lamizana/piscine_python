#####################################################################
# Programme Python ft_calculator                                    #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from ft_calculator import calculator


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    return (0)


#####################################################################
if __name__ == "__main__":
    main()
