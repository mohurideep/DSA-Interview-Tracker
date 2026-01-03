Problem

Given an integer array nums, return indices of the two numbers such that they add up to a given target.

Function signature
def two_sum(nums: list[int], target: int) -> list[int]:
    ...

Rules (read carefully)
Exactly one valid solution exists
You may not use the same element twice
Return indices in any order
Time complexity must be better than O(n²)

Examples
nums = [2, 7, 11, 15], target = 9
→ [0, 1]

nums = [3, 2, 4], target = 6
→ [1, 2]

nums = [3, 3], target = 6
→ [0, 1]

Constraints (important for reasoning)
2 ≤ len(nums) ≤ 10^4
Values can be negative
Target can be negative