# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv   import load
from matplotlib import pyplot as plt
import pandas as pd
import csv

#######################################################################
# definitions locales de fonctions :

def csv_tolist(path: str) -> list:
    """
    Ouverture du fichier CSV, recuperation des donnees.
    retourne une liste:
    """

    with open(path) as f:         
        file = []
        # Chargement des lignes du fichier csv :
        rows = csv.reader(f, delimiter=',') 
        # Stocke les lignes du fichier dans une liste: 
        for row in rows:                            
            file.append(row)
        f.close()

    return(file)


# ------------------------------------------------------------------- #
def years_data(data: list) -> list:
    """
    Recupere les dates et les stocke dans une liste.
    """

    years = []
    for colunm in data[0][1:]:
        try:
            year = int(colunm)
        except ValueError as e:
            print(f"ValueError: {e}")
            exit(1)
        years.append(year)
    
    return(years)


# ------------------------------------------------------------------- #
def country_data(df: pd.DataFrame, country: str) -> list:
    """
    Recupere les esperance de vie en france en fonction
    des annees et les stocke dans une liste.
    """

    data = df.values.tolist()

    expectancy = []
    for row in data:
        if row[0] == country:
            for colunm in row[1:]:
                try:
                    age = float(colunm)
                except ValueError as e:
                    print(f"ValueError: {e}")
                    exit(1)
                expectancy.append(age)

    return(expectancy)


# ------------------------------------------------------------------- #
def main() -> int:
    """
    Fonction progamme principal
    """

    data = (load("../life_expectancy_years.csv"))
    if data is None:
        exit(1)

    # Recupere les donnees pour x et y :
    file_lst = csv_tolist("../life_expectancy_years.csv")
    years = years_data(file_lst)
    life_expectancy = country_data(data, 'France')

    # Tracé de la courbe :
    try:
        plt.plot(years, life_expectancy)
    except ValueError as e:
        print(f"ValueError: {e}")
        exit(1)

    # Fixe le titre du graphique et les libelles des axes :
    plt.title("France life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Years")
    plt.xticks(range(1800, max(years), 40))

    # Affiche le tableau :
    try:
        plt.show()
    except KeyboardInterrupt:
        exit(130)

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
