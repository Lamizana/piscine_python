import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    Fonction qui prend en paramètre un tableau 2D, 
    print sa forme et renvoie une version tronquée du tableau
    en fonction des arguments de début et de fin fournis
    """

    # Verification validite des arguments :
    msg = "AssertionError: list are not list or None"
    try:
        assert isinstance(family, list), msg
        assert family, msg
        int(start) or float(start)
        int(end) or float(end)
    except AssertionError as msg:
        print(msg)
        return
    except ValueError:
        print("ValueError: the value must be an int or float")
        return

    # Creation array 2d :
    array_2d = family[start : end].copy()
      
    print(f"My shape is : {np.shape(family)}")
    print(f"My new shape is : {np.shape(array_2d)}")
     
    return (array_2d)
