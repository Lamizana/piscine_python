# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_image import ft_load

#######################################################################
# definitions locales de fonctions :


def main() -> int:
    """
    Fonction progamme principal
    """

    print(ft_load("landscape.jpg"))
    return (0)


#######################################################################
if __name__ == "__main__":
    main()
