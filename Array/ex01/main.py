# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
from array2D import slice_me

#######################################################################
# definitions locales de fonctions :

def main() -> int:
    """
    Fonction progamme principal
    """
    
family =    [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    main()
