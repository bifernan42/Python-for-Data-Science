def ft_filter(function, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    if function is not None and hasattr(function, '__call__'):
        return [item for item in iterable if function(item) is True]
    else:
        return [item for item in iterable]
