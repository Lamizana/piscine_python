from typing import Any, Callable, Generator, Iterable, T

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