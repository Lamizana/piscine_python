def ft_tqdm(lst: range) -> None:
    """
    Copie de la fonction tqdm avec l'opérateur yield
    """

    counter = 0
    total = len(lst)
    ncols = 64
    for i in lst:
        yield i
        counter += 1
        progress = counter / total
        bar_length = int(ncols * progress)
        bar = "=" * bar_length + "#" * (ncols - bar_length)
        print(f"\r{int(progress * 100)}%|[{bar}]| {counter}/{total}", end="")
