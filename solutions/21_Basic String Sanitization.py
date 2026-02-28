def clean_string(s : str) -> str:
    s = s.strip().lower()
    for ch in s:
        if not ch.isalnum() and not ch.isspace():
            s = s.replace(ch, "")
    return s

#using List comprehension
def clean_string_listcomp(s: str) -> str:
    s = s.strip().lower()
    return ''.join([ch for ch in s if ch.isalnum() and not ch.isspace()])

print(clean_string_listcomp("  Hello, \nWorld!  "))  # Output: "hello world"


#using Regex
def clean_string_regex(s : str) -> str:
    import re
    s = s.strip().lower()
    return re.sub(r'[^a-z0-9\s]', '', s)
# print(clean_string_regex("  Hello, \nWorld!  "))  # Output: "hello world"