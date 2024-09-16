# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from    load_image import ft_load
from    PIL import Image
import  matplotlib.pyplot as plt
import  numpy as np


#######################################################################
# definitions locales de fonctions :
def ft_rotate(array: np.ndarray) -> np.ndarray:

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
    
    # Loading the image
    img = ft_load('animal.jpeg')

    # Stocke ses dimensions :
    h, w, c = img.shape
    new_h = int((h-400)/2)
    new_w = int((w-400)/2)

    # Calcul le nouveau format :
    arr1 = img[new_h:-new_h, new_w:-new_w]

    # transforme en image et affiche :
    rota = ft_rotate(arr1)

    data = Image.fromarray(rota)
    print(f"New shape after slicing: {data.size}")
    print(rota[0:1,:,0:1])
    try:
        plt.imshow(data)
        plt.show()
    except KeyboardInterrupt:
        exit(130)
    
    return (0)


#######################################################################
if __name__ == "__main__":
    main()
