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
    Charge les fichiers et affiche la projection de l'espérance de vie par
    rapport au produit national brut de l'année 1900 pour chaque pays.
    """

    file = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    df_income = (load(file))
    df_life = (load("../life_expectancy_years.csv"))
    if df_income is None or df_life is None:
        return (1)

    # Recupere les informations de la colonne 1900 :
    life = df_life['1900'].values.tolist()
    income = df_income['1900'].values.tolist()

    # Tracé de la courbe :
    try:
        plt.plot(income, life, marker='o', linestyle='None', color='b')
    except ValueError as e:
        print(f"ValueError: {e}")
        return (1)

    # Fixe le titre du graphique et les libelles des axes :
    plt.title("1900")
    plt.ylabel("Life expectancy")
    plt.xlabel("Gross domestic product")

    # pour couvrir plusieurs odres de grandeur, Échelle Logarithmique :
    plt.xscale('log')
    plt.xticks([300, 1_000, 10_000], ['300', '1k', '10k'])

    # Affiche le tableau :
    try:
        plt.show()
    except KeyboardInterrupt:
        return (130)

    return (0)


#######################################################################
if __name__ == "__main__":
    main()
