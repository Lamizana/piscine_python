#####################################################################
# Fonction Python : my first decorating [Module Dot]                #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################

def callLimit(limit: int):
    """
    Decorateur qui prend comme argument une limite d'appel
    et qui bloque son exécution.
    """

    count = 0

    def callLimiter(function):
        """Limite le nombres d'appels d'une fonction."""

        def limit_function(*args: any, **kwds: any):
            """Bloque la fonction au dela d une certaine limite"""

            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return (function(*args, **kwds))

        return (limit_function)

    return (callLimiter)
