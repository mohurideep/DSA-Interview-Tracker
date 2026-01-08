Problem

Given an array nums, return an array output where:

output[i] = product of all elements of nums except nums[i]

Constraints
Must be O(n)
Must be no division
Output array allowed
Extra space (besides output) must be O(1)

Function signature
def product_except_self(nums: list[int]) -> list[int]:
    ...

Examples
[1,2,3,4] → [24,12,8,6]
[0,0] → [0,0]
[0,1,2,3] → [6,0,0,0]