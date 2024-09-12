# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from ft_package import count_in_list

#######################################################################


def main() -> int:
    """
    Fonction programme principal
    """

    print(count_in_list(["toto", "tata", "toto"], "toto"))
    print(count_in_list(["toto", "tata", "toto"], "tata"))
    return (0)


if __name__ == "__main__":
    main()
