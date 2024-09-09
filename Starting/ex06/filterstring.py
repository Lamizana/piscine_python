# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# Definitions locales de fonctions :


def check_argv() -> None:
    """Verifie le nombre d'arguments (2 requis) ainsi que leur validite"""

    msg = "AssertionError: the arguments are bad"
    try:
        assert (len(sys.argv) == 3), msg
        int(sys.argv[2].strip())
    except AssertionError as msg:
        print(msg)
        sys.exit(1)
    except ValueError:
        print(msg)
        sys.exit(1)


def ft_filter(func, sequence):
    """ Filtre une sequence en fonction de la fonction donnee"""

    if (func is None):
        yield (x for x in sequence if x)
    else:
        yield (x for x in sequence if func(x) is True)



def main() -> int:
    """Fonction programme principal"""

    check_argv()
    list_argv = (sys.argv[1].split(" "))
    len_word = int(sys.argv[2])
    print(f"Arguments listes:\n{list_argv}")
    print(f"Longueur des mots demande: {len_word}")
    result = (ft_filter(lambda word: len(word) > len_word, list_argv))
    result2 = (filter(lambda word: len(word) > len_word, list_argv))

    print((result))
    print((result2))



#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())
