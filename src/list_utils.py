def remove_unique_elements(my_list):
    """
    Remove unique elements from a list of integers, keeping only elements 
    that appear more than once.

    Args:
        my_list (list): A list of integers to process.

    Returns:
        list: A new list containing only elements that appear multiple times.

    Examples:
        >>> remove_unique_elements([1, 2, 2, 3, 3, 4])
        [2, 3]
        >>> remove_unique_elements([1, 2, 3, 4])
        []
        >>> remove_unique_elements([])
        []
    """
    # Use list comprehension to keep only elements with count > 1
    return [x for x in set(my_list) if my_list.count(x) > 1]