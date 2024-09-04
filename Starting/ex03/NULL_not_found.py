def NULL_not_found(object: any) -> int:
    """ imprime le type d'objet de tous les types de Null."""

    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, bool):
        if object:
            return(1)
        print(f"Fake: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, float):
        if object:
            if str(object) != 'nan':
                return(1)
        print(f"Cheese: {object} {type(object)}")
        return(0)
    
    elif isinstance(object, int):
        if object:
            return(1)
        print(f"Zero: {object} {type(object)}")
        return(0)

    elif isinstance(object, str):
        if object:
            return(1)
        print(f"Empty: {object} {type(object)}")
        return(0)
    
    else:
        print("Type not found")
    
    return(1)
