# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import pandas as pd

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """

    data = pd.read_csv('../life_expectancy_years.csv')
   
    print(type(data))

    # Affiche le debut du fichier :
    # print(data.head())

    # print(data.tail())
    
    # print(data.describe())
    print(data.info())

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
