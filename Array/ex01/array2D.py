import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Fonction qui prend en paramètre un tableau 2D,
    print sa forme et renvoie une version tronquée du tableau
    en fonction des arguments de début et de fin fournis
    """

    # Verification validite des arguments :
    msg = "AssertionError: an argument is invalid or None"
    try:
        for c in family:
            assert len(c) == len(family[0]), msg
        assert isinstance(family, list), msg
        assert isinstance(start, int), msg
        assert isinstance(end, int), msg
    except AssertionError as msg:
        print(msg)
        exit(1)
    except TypeError as msg:
        print("TypeError: ", msg)
        exit(1)
    except ValueError:
        print("ValueError: the value must be an int or float")
        exit(1)

    # Creation array 2d :
    array_2d = family[start: end].copy()

    print(f"My shape is : {np.shape(family)}")
    print(f"My new shape is : {np.shape(array_2d)}")

    return (array_2d)
