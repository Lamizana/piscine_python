#####################################################################
# Programme Python : my first decorating [Module Dot]               #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################
# Importations de fonctions externes :
from callLimit import callLimit


#####################################################################
# definitions locales de fonctions :
def main() -> int:
    """
    Fonction programme principal.
    """

    @callLimit(3)
    def f():
        print ("f()")

    @callLimit(1)
    def g():
        print ("g()")
            
    for i in range(3):
        f()
        g()
        
    return (0)


#####################################################################
if __name__ == "__main__":
    main()