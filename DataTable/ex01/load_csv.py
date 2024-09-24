import csv
import pandas as pd


def load(path: str) -> list: 
    """
    Fonction qui prend un chemin comme argument,
    écrit les dimensions de l'ensemble de données et le renvoie.
    """

    msg = "AssertionError: file's format is invalid or None"
    try:
        assert path[-3:] == "csv", msg
        with open(path,newline='') as file:
            data = []
            tab_csv = csv.reader(file)
            for row in tab_csv:
                data.append(row)
    except AssertionError as msg:
        print(msg)
        return(None)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return (None)
    except TypeError as e:
        print(f"TypeError: {e}")
        return (None)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        return (None)
    
    print("Loading dataset of dimensions", end=' ')
    print(f"({len(data) - 1}, {len(data[1])})")      
    return(data)


def load_pandas(path: str) -> list: 
    """
    Fonction qui prend un chemin comme argument,
    écrit les dimensions de l'ensemble de données et le renvoie.
    """

    msg = "AssertionError: format invalid"
    # Ouverture d'un fichier CSV :
    try:
        tab_csv = pd.read_csv(path)
        assert path[-3:] == "csv", msg
    except AssertionError as msg:
        print(msg)
        return(None)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return (None)

    print(f"Loading dataset of dimensions {tab_csv.shape}")
            
    return(tab_csv)


