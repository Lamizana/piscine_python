#####################################################################
# Programme Python Type                                             #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from load_csv import load
from matplotlib import pyplot as plt


#######################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction progamme principal.
    Charge le fichier 'life_expectancy_years.csv'
    et affiche les informations sur le pays de votre campus.
    """

    data = (load("../life_expectancy_years.csv"))
    if data is None:
        return (1)

    # Recupere les donnees pour x et y :
    years = data.columns[1:].astype(int).tolist()
    life_expectancy = data.iloc[58, 1:].values.tolist()

    # Tracé de la courbe :
    try:
        plt.plot(years, life_expectancy)
    except ValueError as e:
        print(f"ValueError: {e}")
        return (1)

    # Fixe le titre du graphique et les libelles des axes :
    plt.title("France life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.xticks(range(1800, max(years), 40))

    # Affiche le tableau :
    try:
        plt.show()
    except KeyboardInterrupt:
        return (130)

    return (0)


#######################################################################
if __name__ == "__main__":
    main()
