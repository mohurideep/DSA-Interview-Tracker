def remove_duplicates(nums : list[int]) -> list[int]:
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


# one line pythonic solution
def remove_duplicates_dict(nums: list[int]) -> list[int]:
    return list(dict.fromkeys(nums))


print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))  # Output: [1, 2, 3, 4, 5]