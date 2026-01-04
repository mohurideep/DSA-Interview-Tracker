Problem

Given a string s, return the length of the longest substring without repeating characters.

Function signature
def length_of_longest_substring(s: str) -> int:
    ...

Examples
"abcabcbb" -> 3   # "abc"
"bbbbb"    -> 1   # "b"
"pwwkew"   -> 3   # "wke"
""         -> 0
"abba"     -> 2   # "ab" or "ba"

Rules
Must be O(n) time
Must be O(min(n, alphabet)) space
No brute force checking all substrings