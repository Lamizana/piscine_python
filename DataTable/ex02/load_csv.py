#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2224                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Fonction qui prend un tableau csv comme argument,
    écrit les dimensions de l'ensemble de données et le renvoie
    en pd.DataFrame.
    """

    # Ouverture d'un fichier CSV :
    msg = "AssertionError: format invalid or None"
    try:
        assert path, msg
        assert isinstance(path, str), msg
        assert path[-4:] == ".csv", msg
        tab_csv = pd.read_csv(path)
    except AssertionError as msg:
        print(msg)
        return (None)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return (None)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        return (None)
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return (None)

    print(f"Loading dataset of dimensions {tab_csv.shape}")
    return (tab_csv)
