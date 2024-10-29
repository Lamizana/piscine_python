# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

#######################################################################
# definitions locales de fonctions :


def main() -> int:
    """
    Fonction progamme principal
    """

    img_array = ft_load("./landscape.jpg")
    print(img_array)

    ft_invert(img_array)
    ft_red(img_array)
    ft_green(img_array)
    ft_blue(img_array)
    ft_grey(img_array)

    print(ft_invert.__doc__)

    return (0)


#######################################################################
if __name__ == "__main__":
    main()
