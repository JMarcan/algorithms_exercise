def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int = None
    max_int = None
    
    for i, element in enumerate(ints):
        if i == 0:
            min_int = element
            max_int = element
        else:
            if element < min_int:
                min_int = element
            if element > max_int:
                max_int = element
    
    return (min_int, max_int)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")