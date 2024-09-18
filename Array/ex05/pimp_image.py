import numpy as np

def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    
    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (255 - red, 255 - green, 255 - blue)

    return (img)


def ft_red(array: np.array) -> np.array:
    """Change in red the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (red, 0,0)

    return (img)


def ft_green(array: np.array) -> np.array:
    """Change in green the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (0, green,0)

    return (img)


def ft_blue(array: np.array) -> np.array:
    """Change in blue the color of the image received."""

    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (0, 0,blue)

    return (img)


def ft_grey(array: np.array) -> np.array:
    """Change in grey the color of the image received."""
   
    # L’intensité du gris est tout simplement celle du vert :
    rows, colunms, c = array.shape
    img = array.copy()
    for row in range(rows):
        for colunm in range(colunms):
            red, green, blue = img[row][colunm]
            img[row, colunm] = (green, green, green)

    return (img)
