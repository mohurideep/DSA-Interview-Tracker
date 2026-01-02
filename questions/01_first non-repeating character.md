Problem

Given a string s, return the first non-repeating character.
If none exists, return None.

Function signature
def first_unique_char(s: str) -> str | None:
    ...

Examples
"leetcode" → "l"
"aabbcc"   → None
"aabccd"   → "b"
""         → None

Rules (important)

Case-sensitive ("A" ≠ "a")

You must scan the string at most twice

No sorting

No libraries like collections.Counter