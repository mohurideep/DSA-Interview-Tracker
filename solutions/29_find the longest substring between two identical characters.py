def longest_between_equal_chars(s: str) -> int:
    first_char = {}
    max_length = -1
    for i, ch in enumerate(s):
        if ch in first_char:
            max_length = max(max_length, i - first_char[ch] - 1)
        else:
            first_char[ch] = i
    return max_length

print(longest_between_equal_chars("aa"))  # Output: 0
print(longest_between_equal_chars("bderdb"))  # Output: 4
print(longest_between_equal_chars("abcdef"))  # Output: -1