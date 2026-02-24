def quick_sort(nums : list[int]) -> list[int]:
    """
Pick a pivot → put it in the correct position → recursively sort left and right parts.
Instead of breaking the array evenly, Quick Sort organizes the array around one element.
That element is called the pivot.

What is a Pivot?

A pivot is just a chosen element (often last or first element).

Example:

[5, 2, 9, 1, 5, 6]

Pick pivot = 6

We rearrange the array so:

(all elements < 6) + 6 + (all elements > 6)

Result:

[5, 2, 1, 5] 6 [9]

Now 6 is already in its final sorted position.

We only need to sort the left and right parts.
    """
#Lomuto Partition Algo
def partition(nums : list[int], low : int, high : int):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    #place the pivot in the correct position
    nums[i+1],nums[high] = nums[high], nums[i+1]
    return i+1

def quick_sort_helper(nums : list[int], low : int, high : int):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort_helper(nums, low, pivot_index - 1)
        quick_sort_helper(nums, pivot_index + 1, high)
    return nums

def quick_sort(nums : list[int]) -> list[int]:
    return quick_sort_helper(nums, 0, len(nums) - 1)


print(quick_sort([5,2,9,1,5,6]))