# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv   import load
from matplotlib import pyplot as plt
import pandas as pd

#######################################################################
# definitions locales de fonctions :

def years_data(df: pd.DataFrame) -> list:
    """
    Recupere les dates et les stocke dans une liste.
    """

    # rrecupere les informations de la 1er ligne :
    year_df = df.columns.tolist()

    years = []
    for colunm in year_df[1:]:
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
    Fonction progamme principal.
    Charge le fichier 'life_expectancy_years.csv'
    et affiche les informations sur le pays de votre campus.
    """

    data = (load("../life_expectancy_years.csv"))
    if data is None:
        exit(1)

    # Recupere les donnees pour x et y :
    years = years_data(data)
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
    plt.xlabel("Year")
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
