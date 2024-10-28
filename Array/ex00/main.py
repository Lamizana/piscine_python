# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from give_bmi import give_bmi, apply_limit

#######################################################################
# definitions locales de fonctions :


def main() -> int:
    """
    Fonction progamme principal
    """

    height = [2, 1.15 ,3]
    weight = [165.3, 38.4, 45]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

#######################################################################

if __name__ == "__main__":
    main()
