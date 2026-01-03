Problem

Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Function signature
def subarray_sum_count(nums: list[int], k: int) -> int:
    ...

Examples
nums = [1, 1, 1], k = 2
output = 2
# subarrays: [1,1] (0..1), [1,1] (1..2)

nums = [1, 2, 3], k = 3
output = 2
# subarrays: [1,2], [3]

nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
output = 4

Constraints
1 ≤ len(nums) ≤ 2 * 10^4
values can be negative
k can be negative