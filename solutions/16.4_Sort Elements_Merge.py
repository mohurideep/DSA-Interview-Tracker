def merge_sort(nums : list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])

    return merge(left_half, right_half)

def merge(left : list[int], right : list[int]) -> list[int]:
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged



print(merge_sort([5, 2, 9, 1]))