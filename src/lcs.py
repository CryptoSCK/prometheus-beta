def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the Longest Common Subsequence (LCS) between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Find the maximum LCS length
    max_length = dp[m][n]
    
    # Backtrack to find all possible LCS with maximum length
    def backtrack(max_lcs):
        candidates = []
        def find_candidates(i, j, current_lcs):
            # If we've built a full length subsequence
            if len(current_lcs) == max_length:
                candidates.append(current_lcs)
                return
            
            # Try to extend the current subsequence
            for x in range(i, m):
                for y in range(j, n):
                    if str1[x] == str2[y]:
                        # Check if this char maintains the subsequence property
                        if not current_lcs or (current_lcs and 
                           (str1.index(str1[x]) > str1.index(current_lcs[-1]) and 
                            str2.index(str2[y]) > str2.index(current_lcs[-1]))):
                            find_candidates(x+1, y+1, current_lcs + str1[x])
        
        find_candidates(0, 0, "")
        return candidates
    
    # Return the lexicographically first LCS
    possible_lcs = backtrack(max_length)
    return sorted(possible_lcs)[0] if possible_lcs else ""