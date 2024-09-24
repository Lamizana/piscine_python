# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv   import load
from matplotlib import pyplot as plt

#######################################################################
# definitions locales de fonctions :

def years_data(data: list) -> list:
    """
    Recupere les dates et les stocke dans une liste
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


def french_data(data: list) -> list:
    """
    Recupere les esperance de vie en france en fonction
    des annees et les stocke dans une liste
    """

    expectancy = []
    for row in data:
        if row[0] == 'France':
            for colunm in row[1:]:
                try:
                    age = float(colunm)
                except ValueError as e:
                    print(f"ValueError: {e}")
                    exit(1)
                expectancy.append(age)

    return(expectancy)


def main() -> int:
    """
    Fonction progamme principal
    """

    data = (load("../life_expectancy_years.csv"))
    if data is None:
        exit(1)

    years = years_data(data)
    life_expectancy = french_data(data) 

    fig, ax = plt.subplots()
    plt.plot(years, life_expectancy)

    # Fixe le titre du graphique et les libelles des axes :
    ax.set_title("France life expectancy Projections")
    ax.set_xlabel("Years")
    ax.set_ylabel("Life expectancy")

    # Fixe la taille des graduations :
    ax.tick_params(axis='both', labelsize=11)

    # Affiche le tableau :
    try:
        plt.show()
    except KeyboardInterrupt:
        exit(130)

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
