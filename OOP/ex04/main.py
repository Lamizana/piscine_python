#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#####################################################################
from ft_calculator import calculator


def main() -> int:
    """
    Fonction programme principal.
    """
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a,b)
    calculator.add_vec(a,b)
    calculator.sous_vec(a,b)


#####################################################################
if __name__ == "__main__":
    main()