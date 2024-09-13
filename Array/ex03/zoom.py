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
    print(f"New shape after slicing: {arr1[:,:,0:1].shape}")

    d = arr1[0:1,:,0:1]
    print(d)

    # transforme en image et affiche :
    data = im.fromarray(arr1)
    try:
        plt.imshow(data)
        plt.show()
    except KeyboardInterrupt:
        exit(130)
    
    return (0)

#######################################################################
if __name__ == "__main__":
    main()
