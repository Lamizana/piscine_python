def count_in_list(lst: list, word: str) -> int:
    """
    Compte le nombre d element donne dans une liste
    """

    count = 0
    if (lst is None or word is None):
        return (count)
    
    for name in lst:
        if name == word:
            count += 1       
    return (count)
