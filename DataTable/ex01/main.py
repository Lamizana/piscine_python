# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv import load
from load_csv import load_pandas

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """

 
    data = (load("../life_expectancy_years.csv"))
    
    print(data)
    # print(type(data))

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
