def NULL_not_found(object: any) -> int:
    """ imprime le type d'objet de tous les types de Null."""

    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
        return(0)

    elif isinstance(object, str):
        if object is not Empty:
            print("Type not Found")
            return(1)
        print(f"Empty: {object} {type(object)}")
        return(0)
    
    else:
        print("Type not found")
    
    return(1)

#-----------------------------------------------------------------------------#

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))


# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>