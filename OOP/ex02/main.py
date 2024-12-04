#####################################################################
# Programme Python DiamondTrap                                      #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from DiamondTrap import King


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)

    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    return (0)


#####################################################################
if __name__ == "__main__":
    main()
