def ft_filter(func, sequence) -> iter:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if (func is None):
        return (sequence)
    else:
        result = (x for x in sequence if func(x) is True)
        return (result)
