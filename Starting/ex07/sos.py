# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# definitions locales de focntions :
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


def check_argv() -> None:
    """
    Verifie le nombre d'arguments (1 requis) ainsi que leur validite
    """

    msg = "AssertionError: the arguments are bad"
    try:
        assert (len(sys.argv) == 2), msg
        for c in sys.argv[1]:
            assert c.isalnum() or c.isspace(), msg
            assert str(NESTED_MORSE.get(c.title())) != "None", msg
    except AssertionError as msg:
        sys.exit(msg)


def translate_in_morse(object: str) -> None:
    """
    Prend une chaîne de caractères comme argument
    et l'encode en code morse
    """

    msg = ""
    for c in object:
        msg += (NESTED_MORSE.get(c.title()))
    print(msg.rstrip())


def main() -> int:
    """
    Fonction programme prinipal
    """

    check_argv()
    translate_in_morse(sys.argv[1])
    return (0)


#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())
