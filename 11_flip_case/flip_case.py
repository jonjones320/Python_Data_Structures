def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = phrase.lower()
    to_swap = to_swap.lower()
    output = ""
    
    for ltr in phrase:
        if ltr == to_swap:
            output = output + ltr.swapcase()
    return output