#####################################################################
# Programme Python S1E9                                             #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from S1E9 import Stark


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)

    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")

    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    # hodor = Character("hodor")

    return (0)


#####################################################################
if __name__ == "__main__":
    main()
