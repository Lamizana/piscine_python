
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    # """
    # Prend 2 listes d'entiers ou de flottants en entrée
    # et renvoie une liste de valeurs d'IMC.
    # La formule est : IMC = Poids / (Taille x Taille)
    # """
    """ Prend une liste d'entiers ou de flottants 
    et un entier représentant une limite comme paramètres.
    Args:
        bmi (list[int |  float]): liste d'entiers ou de flottants 
        limit (int): _description_

    Returns:
        list[bool]: Renvoie une liste de booléens :
        - True si la limite est dépassée
    """
    lst = []
    msg = "AssertionError: the lists are not the same size"
    try:
        assert len(height) == len(weight), msg
        for poid, taille in zip(weight, height):
            int(poid) or float(poid)
            int(taille) or float(taille)
            imc = poid / (taille * taille)
            lst.append(imc)
    except AssertionError as msg:
        print(msg)
        return
    except ValueError:
        print("ValueError: the value must be an int or float")
        return
    except ZeroDivisionError:
        print("ZeroDivisionError: division by 0 not possible")
        return
    except TypeError:
        print("TypeError: argument is 'NoneType'")
        return

    return (lst)


def apply_limit(bmi: list[int | float],
                limit: int) -> list[bool]:
    """
    Prend une liste d'entiers ou de flottants 
    et un entier représentant une limite comme paramètres.
    Renvoie une liste de booléens (True si la limite est dépassée).
    """

    lst = []
    msg = "AssertionError: limit is negative"
    try:
        int(limit)
        assert limit >= 0, msg
        for x in bmi:
            int(x) or float(x)
            if (x > limit):
                lst.append(True)
            else:
                lst.append(False)
    except AssertionError as msg:
        print(msg)
        return 
    except ValueError:
        print("ValueError: the value must be an int or float")
        return
    except TypeError:
        print("TypeError: argument is 'NoneType'")
        return
    return (lst)
