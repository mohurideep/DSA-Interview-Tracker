Problem

Given an integer array nums, return the maximum sum of any contiguous subarray of size k.

Function signature
def max_sum_subarray(nums: list[int], k: int) -> int:
    ...

Examples
nums = [2, 1, 5, 1, 3, 2], k = 3 → 9   # [5,1,3]
nums = [2, 3, 4, 1, 5], k = 2 → 7     # [3,4]
nums = [1, 1, 1, 1], k = 2 → 2

Rules
Assume k <= len(nums)
All numbers can be positive or negative
Time must be O(n) (no nested loops)