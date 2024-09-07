# -*-coding:Utf-8 -*
#######################################################################
# Importations de fonctions externes :
import sys
from typing import Any, Callable, Generator, Iterable, T
#######################################################################
# Definitions locales de fonctions :
s_red = "\033[4;31m"
white = "\033[0m"


def check_argv() -> None:
    """Verifie le nombre d'arguments (2 requis) ainsi que leur validite"""

    msg = f"{s_red}AssertionError: the arguments are bad{white}"
    try:
        assert (len(sys.argv) == 3), msg
        assert not isinstance(sys.argv[2], (int)), msg
    except AssertionError as msg:
        print(msg)
        sys.exit(1)




def my_filter(func: Callable[[T], Any], iterable: Iterable[T]) -> Generator[T, None, None]:
    """Yields all values from the iterable for which the function returns a truthful value"""
    
    for value in iterable:
        if func(value):
            yield value

def ft_filter(func, sequence):
    result = []
    for i in sequence:
        if func(i) is True:
            result.append(i)
    return result


def main() -> int:
    """Fonction programme principal"""

    check_argv()

    personnes = [18, 23, 42, 61, 88]

    # travailleurs = filter(lambda age: age <= 62, personnes)
    titi = my_filter(lambda age: age <= 62, personnes)
    toto = ft_filter(lambda age: age <= 62, personnes)
    
    

    n = 2
    t = (sys.argv[1].split(" "))
    print(t)
    words = filter(lambda word: len(word) > 4, t)
    words2 = [word for word in t if len(word) < 2]
    
    # print(list(travailleurs))
    print(list(titi))
    print(list(toto))
    
    
    print(list(words))
    print(list(words2))
    


#######################################################################
# Corps principal du programme :
if __name__ == "__main__":
    sys.exit(main())

