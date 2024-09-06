# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys

#######################################################################
# Definitions locales de fonctions :
s_red = "\033[4;31m"
white = "\033[0m"


def number_argv() -> None:
    """Verifie le nombre d'arguments, 1 requis"""

    msg = f"{s_red}AssertionError: only one argument required{white}"
    try:
        assert (len(sys.argv) <= 2), msg
    except AssertionError as msg:
        print(msg)
        sys.exit(1)


def request_argv() -> str:
    """Demande une chaine de caractere a l utilisateur"""

    msg = ""
    if (len(sys.argv) == 1 or len(sys.argv[1]) == 0):
        while (len(msg) == 0):
            try:
                print("What is the text to count?")
                msg = sys.stdin.readline()
            except KeyboardInterrupt:
                print(f"\n{s_red}Control-C: exit{white}")
                sys.exit()
            return (msg)
    return (sys.argv[1])


def standalone(object: str) -> None:
    """Affiche la somme des majuscules, minuscules, des caractères
    de ponctuation, des chiffres et des espaces"""

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
    """Fonction programme principal"""

    number_argv()
    msg = request_argv()
    standalone(msg)


#######################################################################
# Corps principal du programme :

if __name__ == "__main__":
    sys.exit(main())
