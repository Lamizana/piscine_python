def ft_filter(func, sequence) ->any:
    """
    Filtre une sequence en fonction de la fonction donnee
    """

    if (func is None):
        for value in sequence:
            yield value
    else:
        for value in sequence:
            if func(value):
                yield value

