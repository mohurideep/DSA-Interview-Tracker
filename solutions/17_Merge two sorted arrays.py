# Because both arrays are sorted, I can maintain two pointers — one for each array — 
# and repeatedly pick the smaller element. This gives linear time complexity O(n + m), which is optimal.”

def merge_sorted_list(arr1 : list[int], arr2 : list[int]) -> list[int]:
    i = 0
    j = 0
    result = []

    #compare elements from both the array/list
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else :
            result.append(arr2[j])
            j += 1

    # add remaining elements
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])
    return result


print(merge_sorted_list([1,2,3], [4,5,6]))