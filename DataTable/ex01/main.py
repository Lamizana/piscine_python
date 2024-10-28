# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv import load
import pandas as pd


#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """

 
    data = (load("../life_expectancy_years.csv"))
    df = pd.DataFrame(data, columns = ["country"])
    print(df)
    # print(type(data))

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
