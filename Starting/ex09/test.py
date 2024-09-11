# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from ft_package import count_in_list

#######################################################################
def main() -> int:
    """
    Fonction programme principal
    """

    print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tata")) # output: 0
    return (0)


if __name__ == "__main__":
    main()
