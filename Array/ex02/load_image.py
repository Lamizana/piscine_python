import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray: 
    """
    Charge une image, imprime son format et ses pixels au format RGB
    """

    try:
        imgPill = Image.open(path)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        exit(1)
    except AttributeError as e:
        print(f"AttributeError: {e}")
        exit(1)
    # Transformation de l'image en RGB en tableau numpy
    img = np.array(imgPill)
    imgPill.close()

    print(f"The shape of image is: {img.shape}")
    print(img)
    return (img)
    