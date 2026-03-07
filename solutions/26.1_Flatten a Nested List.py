# Bruteforce approach, works on 1 level of nesting
def flattern_list_bruteforce(nested_list : list) -> list:
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            for item in sublist:
                flat_list.append(item)
        else :
            flat_list.append(sublist)
    return flat_list

print(flattern_list_bruteforce([1, [2, 3], [4, [5, 6]], 7]))


def flattern_list_recursive(nested_list : list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flattern_list_recursive(item))
        else:
            flat_list.append(item)
    return flat_list

print(flattern_list_recursive([1, [2, 3], [4, [5, 6]], 7]))