Problem

Given an array nums, return the majority element.

The majority element appears more than [n/2] times.
You may assume the majority element always exists.

Function signature
def majority_element(nums: list[int]) -> int:
    ...

Examples
[3,2,3] → 3
[2,2,1,1,1,2,2] → 2

Rules
Must be O(n) time
Must be O(1) space
⚠️ This constraint matters. Sorting or hashmap is not allowed.