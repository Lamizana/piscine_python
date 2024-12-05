#####################################################################
# Fonction Python : my first decorating [Module Dot]                #
# auteur : A.Lamizana, Angouleme, 2024                              #
# -*-coding:Utf-8 -*                                                #
#                                       https://github.com/Lamizana #
#####################################################################

def callLimit(limit: int):
    """
    """
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            """
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return (function(*args, **kwds))
        return(limit_function)
    return (callLimiter)