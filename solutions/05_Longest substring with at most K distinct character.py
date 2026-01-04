def longest_substring_k_distinct(s:str, k:int) -> int:
    substring={}
    left=0
    max_length=0
    
    if not s and k==0:
        return 0
    
    for right,ch in enumerate(s):
        substring[ch]=substring.get(ch,0)+1
        while len(substring)>k:
            left_char=s[left]
            substring[left_char]-=1
            if substring[left_char]==0:
                del substring[left_char]
            left+=1
        max_length=max(max_length,right-left+1)

    return max_length