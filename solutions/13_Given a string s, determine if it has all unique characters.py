def has_unique_chars( s: str) -> bool:
    seen = ["False"] * 128
    # o[1] space complexity
    for ch in s:
        idx = ord(ch)
        if seen[idx]:
            return False
        seen[idx] = True
    return True

# def has_unique_chars( s: str) -> bool:
#     #o[k] space complexity
#     set_chars = set()
#     for ch in s:
#         if ch in set_chars:
#             return False
#         set_chars.add(ch)
#     return True