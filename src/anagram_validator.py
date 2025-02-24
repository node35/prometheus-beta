def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. This implementation:
    - Is case-sensitive (only works with lowercase letters)
    - Requires both strings to have the same length
    - Checks if both strings contain the same letters in a different order

    Args:
        str1 (str): The first input string (lowercase letters only)
        str2 (str): The second input string (lowercase letters only)

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        ValueError: If input strings contain non-lowercase letters
    """
    # Validate input contains only lowercase letters
    if not (str1.islower() and str2.islower()):
        raise ValueError("Inputs must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Compare character frequencies
    return sorted(str1) == sorted(str2)