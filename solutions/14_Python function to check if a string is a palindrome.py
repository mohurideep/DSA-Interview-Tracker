def is_palindrome(s) -> bool:
    # remove space and normalize case
    s = s.replace(" ", "").lower()

    #compare string with its reverse
    return s == s[::-1]


# 2 pointer approach
def is_plaindrome_2pointer(s) -> bool:
    s = s.replace(" ","").lower()
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_plaindrome_2pointer("madam")) 