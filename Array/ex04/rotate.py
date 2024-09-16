# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_image import ft_load
from PIL import Image as im 
import matplotlib.pyplot as plt

#######################################################################
# definitions locales de fonctions :

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
    lignes, colonnes, k = arr1.shape

    data = im.fromarray(arr1)
    print(f"New shape after slicing: {data.size}")

    rotateArr = arr1.copy()
    for x in range(0,colonnes):
        for y in range(0,lignes):
            rotateArr[colonnes-x-1][lignes-y-1] = arr1[x][y]

    data2 = im.fromarray(rotateArr)

    try:
        plt.imshow(data2)
        plt.show()
    except KeyboardInterrupt:
        exit(130)
    
    return (0)
    d = arr1[0:1,:,0:1]
    # print(d)



#######################################################################
if __name__ == "__main__":
    main()
