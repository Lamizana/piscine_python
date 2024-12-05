#####################################################################
# Programme Python : Outer_inner [Module Dot]                       #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from in_out import outer
from in_out import square
from in_out import pow


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
    return (0)


#####################################################################
if __name__ == "__main__":
    main()