def count_substring_occurrences(string: str, substring: str) -> int:
    """
    Count the number of times a substring occurs in a given string.
    
    This function uses the KMP (Knuth-Morris-Pratt) algorithm to achieve O(n) time complexity,
    where n is the length of the input string.
    
    Args:
        string (str): The main string to search in
        substring (str): The substring to count occurrences of
    
    Returns:
        int: The number of times the substring appears in the string
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If substring is an empty string
    """
    # Input validation
    if not isinstance(string, str) or not isinstance(substring, str):
        raise TypeError("Both inputs must be strings")
    
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    # If substring is longer than string, no occurrences possible
    if len(substring) > len(string):
        return 0
    
    # Compute the KMP failure function (prefix table)
    def compute_lps(pattern):
        """Compute the Longest Proper Prefix which is also Suffix (LPS) array."""
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    # Compute LPS array for the substring
    lps = compute_lps(substring)
    
    # KMP search to count occurrences
    occurrences = 0
    i = 0  # index for string
    j = 0  # index for substring
    
    while i < len(string):
        if substring[j] == string[i]:
            i += 1
            j += 1
        
        # Substring fully matched
        if j == len(substring):
            occurrences += 1
            # Move j back using LPS
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(string) and substring[j] != string[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return occurrences