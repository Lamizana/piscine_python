# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from load_csv import load
from load_csv import load_pandas
import matplotlib.pyplot as plt

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """

    data = (load("../life_expectancy_years.csv"))
    # my_country = [row for row in data if row == 'France']
    # my_country = []
    for row in data:
        if row[0] == 'France':
            my_country = row[1:]
            break
    print(type(my_country))
    
    # print(plt.style.available)
    # plt.style.use('seaborn-v0_8-dark')
    # fig, ax = plt.subplots()
    # ax.plot(my_country)
    plt.plot((my_country))
    plt.show()
    return (0)

#######################################################################
if __name__ == "__main__":
    main()
