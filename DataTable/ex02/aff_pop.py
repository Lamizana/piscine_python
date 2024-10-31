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
    Recupere la population du pays en fonction
    des annees et les stocke dans une liste.
    """

    data = df.values.tolist()
    population = []
    for row in data:
        if row[0] == country:
            for colunm in row[1:]:
                try:
                    people = float(colunm[:-1])
                    if colunm[-1] == 'M':
                        people *= 10**6
                    elif colunm[-1] == 'K':
                        people *= 10**3
                except ValueError as e:
                    print(f"ValueError: {e}")
                    exit(1)
                population.append(int(people))

    return(population)


# ------------------------------------------------------------------- #
def main() -> int:
    """
    Fonction progamme principal
    """

    data = (load("../population_total.csv"))
    if data is None:
        exit(1)

    # Recupere les donnees pour x et y :
    file_lst = csv_tolist("../population_total.csv")
    years = years_data(file_lst)

    people_fr = country_data(data, 'France')
    people_bf = country_data(data, 'Burkina Faso')

    # Stocke les valeurs de 1800 a 2050, soit 250 colonnes :
    years = years[:250]
    people_fr = people_fr[:250]
    people_bf = people_bf[:250]

    # Tracé des differentes courbes :
    try:
        plt.plot(years, people_bf, 'b', label="Burkina Faso")
        plt.plot(years, people_fr, 'r', label="France")
        plt.legend()
        # plt.legend(loc="lower right")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Fixe le titre du graphique et les libelles des axes :
    plt.title("Population Projections")
    plt.ylabel("population")
    plt.xlabel("Year")

    # Spécifier des valeurs précises pour les graduations de l'axe X et Y :
    plt.xticks(range(1800, 2050, 40))
    plt.yticks([20_000_000, 40_000_000, 60_000_000],['20M', '40M', '60M'])

    # Affiche le tableau :
    try:
        plt.show()
    except KeyboardInterrupt:
        exit(130)

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
