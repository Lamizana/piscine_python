# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# Definitions locales de fonctions :

def number_argv() -> None:
    """
    Verifie le nombre d'arguments, 1 requis
    """

    msg = f"AssertionError: only one argument required"
    try:
        assert (len(sys.argv) <= 2), msg
    except AssertionError as msg:
        sys.exit(msg)


def request_argv() -> str:
    """
    Demande une chaine de caractere a l utilisateur
    """

    msg = ""
    if (len(sys.argv) == 1 or len(sys.argv[1]) == 0):
        while (len(msg) == 0):
            try:
                print("What is the text to count?")
                msg = sys.stdin.readline()
            except KeyboardInterrupt:
                sys.exit(f"\nControl-C: exit")
            return (msg)
    return (sys.argv[1])


def standalone(object: str) -> None:
    """
    Affiche la somme des majuscules, minuscules, des caractères
    de ponctuation, des chiffres et des espaces
    """

    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    for letter in object:
        if (letter.islower()):
            lower += 1
        elif (letter.isupper()):
            upper += 1
        elif (letter.isdigit()):
            digit += 1
        elif (letter == " " or letter == '\n'):
            space += 1
        else:
            punctuation += 1

    print(f"The text contains {len(object)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main() -> int:
    """
    Fonction programme principal
    """

    number_argv()
    msg = request_argv()
    standalone(msg)
    return (0)

#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())
