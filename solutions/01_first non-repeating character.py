def first_unique_char(s: str) -> str | None:
    if not s:
        return None
    freq_dict={}
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch,0)+1
    
    for ch in s:
        if freq_dict[ch] == 1:
            return ch
    return None