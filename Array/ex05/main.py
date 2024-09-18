# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from    load_image import ft_load
from    pimp_image import ft_invert
from    pimp_image import ft_red
from    pimp_image import ft_green
from    pimp_image import ft_blue
from    pimp_image import ft_grey
from    PIL import Image 
import  matplotlib.pyplot as plt


#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """

    img_array = ft_load("./landscape.jpg")

    img_INVERT = ft_invert(img_array)
    img_RED = ft_red(img_array)
    img_GREEN = ft_green(img_array)
    img_BLUE = ft_blue(img_array)
    img_GREY = ft_grey(img_array)


    # transforme en image et affiche :
    img = Image.fromarray(img_INVERT)
    try:
        plt.imshow(img)
        plt.show()
    except KeyboardInterrupt:
        exit(130)

    # ft_invert(array)
    # ft_red(array)
    # ft_green(array)
    # ft_blue(array)
    # ft_grey(array)

    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    return (0)

#######################################################################
if __name__ == "__main__":
    main()
