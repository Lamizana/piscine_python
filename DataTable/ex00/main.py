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

 
    print(load_pandas("../life_expectancy_years.csv"))
    
    # print(data.iloc[:,:])
    # print(type(data))

    return (0)

#######################################################################
if __name__ == "__main__":
    main()
