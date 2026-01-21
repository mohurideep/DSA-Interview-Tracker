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


def first_unique_char(s : str) -> str | None:
    if not isinstance(s, str) or not s:
        return None
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count +=1
                if count > 1:
                    break
        if count == 1:
            return i
    return None