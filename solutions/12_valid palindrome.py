def is_palindrome(s: str) -> bool:
    # """
    # Check if the given string is a palindrome, considering only alphanumeric characters and ignoring cases.

    # :param s: Input string
    # :return: True if the string is a palindrome, False otherwise
    # """
    # filtered_string =''

    # for ch in s:
    #     if ch.isalnum():
    #         filtered_string += ch.lower()
    
    # return filtered_string == filtered_string[::-1]
    
    # # filtered_chars = [char.lower() for char in s if char.isalnum()]
    # # return filtered_chars == filtered_chars[::-1] 
    # rejected because not o[1] space complexity
    #below is with 0[1] complexity
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
