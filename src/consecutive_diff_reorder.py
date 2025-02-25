from typing import List, Optional

def reorder_list_with_consecutive_diff(nums: List[int]) -> Optional[List[int]]:
    """
    Reorder a list of integers so that the difference between 
    consecutive elements is always 1, -1, or 0.
    
    Args:
        nums (List[int]): Input list of integers to be reordered
    
    Returns:
        Optional[List[int]]: Reordered list or None if reordering is impossible
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Handle empty or single-element lists
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    
    # Sort the input list to help with reordering
    sorted_nums = sorted(nums)
    
    # Try to construct a valid reordering
    result = [sorted_nums[0]]
    used = {sorted_nums[0]}
    
    while len(result) < len(nums):
        last = result[-1]
        
        # Try to find a valid next number
        found_next = False
        for num in sorted_nums:
            if num in used:
                continue
            
            # Check if the difference is acceptable
            diff = num - last
            if abs(diff) <= 1:
                result.append(num)
                used.add(num)
                found_next = True
                break
        
        # If no valid next number found, try backtracking
        if not found_next:
            # Reset and start with the next possible initial number
            for initial in sorted_nums:
                if initial not in used:
                    result = [initial]
                    used = {initial}
                    break
            else:
                # No possible reordering
                return None
    
    # Verify the result
    for i in range(1, len(result)):
        if abs(result[i] - result[i-1]) > 1:
            return None
    
    return result