def sort_list_selection( nums : list[int]) -> list[int]:
    n = len(nums)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums

print(sort_list_selection([5, 2, 9, 1]))