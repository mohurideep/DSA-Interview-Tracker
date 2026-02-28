def string_sanitization(s):
    s = s.strip().lower()
    return ''.join([ch for ch in s if ch.isalnum() and not ch.isspace()])

def isPalindrome(s):
    cleaned_string = string_sanitization(s)
    return cleaned_string == cleaned_string[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("Hello World"))  # Output: False