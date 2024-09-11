import numpy as np
from PIL.Image import *


def ft_load(path: str): # -> array:  (you can return to the desired format)
    """
    Charge une image, imprime son format et ses pixels au format RGB
    """
    
    img = open("landscape.jpg")
    r,g,b = img.getpixel((0,0))
    print(f"The shape of image is: ({r}, {g}, {b})")
    largeur_image=3
    hauteur_image=3
    
    #Parcours l image et affiche les couleur en RGB :
    for y in range(hauteur_image):
        for x in range(largeur_image):
            r, g, b = img.getpixel((x, y))
            print(r, g , b)
	
    # Image.show(i)
    return 