def flatten_list_stack(nested_list: list) -> list:
    flat_list = []
    stack = list(nested_list)  # shallow copy the list
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            flat_list.append(current)
    return flat_list[::-1]  # reverse the list to maintain original order

print(flatten_list_stack([1, [2, 3], [4, [5, 6]], 7]))



# recursive generator solution
def flatten_list_generator(nested_list: list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
            # above line is responsible for yielding all items from the sublist
            # similar as for x in flatten_list_generator(item)  
            #    yield x
        else:
            yield item

print(list(flatten_list_generator([1, [2, 3], [4, [5, 6]], 7])))
