Problem

Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

Function signature
def longest_substring_k_distinct(s: str, k: int) -> int:
    ...

Examples
s = "eceba", k = 2
output = 3
# "ece"

s = "aa", k = 1
output = 2
# "aa"

s = "a", k = 0
output = 0

s = "abaccc", k = 2
output = 4
# "accc"

Rules
Must be O(n) time
Use a frequency map
Handle edge cases like k = 0, empty string