# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv import load

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """
 
    print(load("../life_expectancy_years.csv"))
    return (0)

#######################################################################
if __name__ == "__main__":
    main()
