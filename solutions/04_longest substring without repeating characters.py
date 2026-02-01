def length_of_longest_substring(s:str) -> int:
    left = 0
    max_len = 0
    last_seen= {}

    if not s:
        return 0
    for right,ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch]+1
        last_seen[ch] = right
        max_len = max(max_len, right-left+1)

    return max_len


def length_of_longest_substring1(s: str) -> int:
    # O(n^3) solution
    if len(s) == 0:
        return 0
    max_count = 1
    for i in range(len(s)):
        count = 1
        for j in range(i+1,len(s)):
            if s[j] in s[i:j]:
                break
            count +=1
        max_count = max(max_count,count)
        
    return max_count


print (length_of_longest_substring1("pwwkew"))