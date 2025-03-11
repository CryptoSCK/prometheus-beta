def cycle_sort(arr):
    """
    Implement the Cycle Sort algorithm for sorting an array in-place.
    
    Cycle sort is an in-place, unstable sorting algorithm that is optimal in terms 
    of the number of memory writes. It minimizes the number of memory writes to sort 
    an array with a given set of values.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (though the sorting happens in-place).
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> cycle_sort([5, 2, 9, 1, 7, 6, 3])
        [1, 2, 3, 5, 6, 7, 9]
        >>> cycle_sort([])
        []
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Perform cycle sort
    for cycle_start in range(len(arr) - 1):
        item = arr[cycle_start]
        
        # Find where to put the item
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position
        if pos == cycle_start:
            continue
        
        # Otherwise, put the item there or right after any duplicates
        while item == arr[pos]:
            pos += 1
        
        # Swap the items
        arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Find where to put the item
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            
            # While there are duplicates, move past them
            while item == arr[pos]:
                pos += 1
            
            # Swap the items
            arr[pos], item = item, arr[pos]
    
    return arr