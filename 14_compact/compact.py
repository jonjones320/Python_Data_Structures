def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst_copy = lst.copy()
    (lst_copy.append(element) for element in lst if element == True)
    return lst_copy