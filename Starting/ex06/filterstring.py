# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# Definitions locales de fonctions :
s_red = "\033[4;31m"
white = "\033[0m"


def check_argv(object: any) -> None:
    """Verifie le nombre d'arguments (2 requis) ainsi que leur validite"""

    msg = f"{s_red}AssertionError: the arguments are bad{white}"
    try:
        assert (len(sys.argv) == 3), msg

    except AssertionError as msg:
        print(msg)
        sys.exit(1)


def main() -> int:
    """Fonction programme principal"""

    check_argv(sys.argv[1])

    personnes = [18, 23, 42, 61, 88]

    travailleurs = filter(lambda age: age <= 62, personnes)

    n = 4
    t = sys.argv[1:]

    word = filter(lambda mot: len(mot) > n, t)
    print(list(travailleurs))
    print(list(word))


#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())

