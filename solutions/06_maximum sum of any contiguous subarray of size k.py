def max_sum_subarray(nums: list[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9

# using Slicing
def max_sum_subarray_slicing(nums: list[int], k: int) -> int:
    max_sum = 0
    for i in range(len(nums) - k + 1):
        max_sum = max(max_sum, sum(nums[i:i + k]))
    return max_sum

    # return max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1))

print(max_sum_subarray_slicing([2, 1, 5, 1, 3, 2], 3))  # Output: 9