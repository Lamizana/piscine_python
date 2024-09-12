# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# definitions locales de fonctions :


def check_argv() -> dict:
    """
    Verifie le nombre d'arguments (1 requis) ainsi que leur validite
    """

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    msg = "AssertionError: the arguments are bad"
    try:
        assert (len(sys.argv) == 2), msg
        for c in sys.argv[1]:
            assert c.isalnum() or c.isspace(), msg
            assert (NESTED_MORSE.get(c.title())), msg
    except AssertionError as msg:
        sys.exit(msg)
    except TypeError as msg:
        sys.exit(msg)

    return (NESTED_MORSE)


def translate_in_morse(object: str) -> None:
    """
    Prend une chaîne de caractères comme argument
    et l'encode en code morse
    """

    morse = check_argv()
    msg = ""
    for c in object:
        msg += (morse.get(c.title()))
    print(msg.rstrip())


def main() -> int:
    """
    Fonction programme prinipal
    """

    translate_in_morse(sys.argv[1])
    return (0)


#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())
