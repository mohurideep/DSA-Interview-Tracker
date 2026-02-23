# using Buble sort 

def sort_list_buble_1(nums: list[int]) -> list[int] :
    # do not use this since it is not a correct bubble sort, since checking outer loop with all the inner loop
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j] :
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

    return nums


def sort_list_buble_2(nums: list[int]) -> list[int] :
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j] , nums [j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


print(sort_list_buble_2([5, 2, 9, 1]))