def ft_filter(func, sequence):
    """Filtre une sequence en fonction de la fonction donnee"""

    if (func is None):
        yield (x for x in sequence if x)
    else:
        yield (x for x in sequence if func(x) is True)
