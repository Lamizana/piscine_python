import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image, imprime son format et ses pixels au format RGB
    """

    msg = "AssertionError: format invalid or None"
    try:
        assert path, msg
        assert isinstance(path, str), msg
        assert path[-3:] == "jpg" or path[-4:] == "jpeg", msg
        imgPill = Image.open(path)
    except AssertionError as msg:
        print(msg)
        exit(1)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        exit(2)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        exit(1)
    except AttributeError as e:
        print(f"AttributeError: {e}")
        exit(1)

    # Transformation de l'image en RGB en tableau numpy
    img = np.array(imgPill)
    imgPill.close()

    print(f"The shape of image is: {img.shape}")
    return (img)
