import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im


# ------------------------------------------------------------------- #
def display(array: np.array, name: str) -> None:
    """Affiche une image"""

    img = im.fromarray(array)
    try:
        plt.title(label=name, fontweight="bold")
        plt.imshow(img)
        plt.show()
    except KeyboardInterrupt:
        exit(130)
    return


# ------------------------------------------------------------------- #
def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (255 - red, 255 - green, 255 - blue)

    display(img, "FT_INVERT")
    return (img)


# ------------------------------------------------------------------- #
def ft_red(array: np.array) -> np.array:
    """Change in red the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (red, 0, 0)

    display(img, "FT_RED")
    return (img)


# ------------------------------------------------------------------- #
def ft_green(array: np.array) -> np.array:
    """Change in green the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (0, green, 0)

    display(img, "FT_GREEN")
    return (img)


# ------------------------------------------------------------------- #
def ft_blue(array: np.array) -> np.array:
    """Change in blue the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (0, 0, blue)

    display(img, "FT_BLUE")
    return (img)


# ------------------------------------------------------------------- #
def ft_grey(array: np.array) -> np.array:
    """Change in grey the color of the image received."""

    # L’intensité du gris est tout simplement celle du vert :
    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (green, green, green)

    display(img, "FT_GREY")
    return (img)
