# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import gi

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """
    
    # imgPill = Image.open("./animal.jpeg")

    # print(type(imgPill))
    # imgPill.show()


    img = np.asarray(Image.open('animal.jpeg'))
    print(repr(img))
    # Loading the image

    imgplot = plt.imshow(img)


    return (0)

#######################################################################
if __name__ == "__main__":
    main()
