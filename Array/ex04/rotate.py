# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from    load_image import ft_load
from    PIL import Image as im
import  matplotlib.pyplot as plt
import  numpy as np


#######################################################################
# definitions locales de fonctions :

def zoom(array: np.array) -> im.Image:
    """
    charge l'image, imprime quelques informations à son sujet 
    et la zoom.
    """

    # transforme l'array en PIL.image :
    image_pil = im.fromarray(array)

    # Recupere les point pour le zoom :
    left = 450
    top = 100
    right = 850
    bottom = 500

    # Zoom sur les postions donnees :
    img_crop = image_pil.crop((left, top, right, bottom))
    print(f"New shape after slicing: {img_crop.size}")

    return (img_crop)


def ft_rotate(array: np.array) -> np.array:

    rows = len(array)
    columns = len(array[0])
    matrice = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(array[i][j])
        matrice.append(row)

    result = np.array(matrice)
    return (result)


def main() -> int:
    """
    Fonction progamme principal
    """
    
    # Charge et zoom l'image :
    img_pil = ft_load('animal.jpeg')
    img = zoom(img_pil)
    
    array = np.array(img)
    print(array[0:1,:,0:1])
    
    # rotation de l'image :
    img_rotate = ft_rotate(array)

    data = im.fromarray(img_rotate)
    print(f"New shape after Transpose: {data.size}")
    print(img_rotate)

    try:
        plt.imshow(data)
        plt.show()
    except KeyboardInterrupt:
        exit(130)
    
    return (0)


#######################################################################
if __name__ == "__main__":
    main()
