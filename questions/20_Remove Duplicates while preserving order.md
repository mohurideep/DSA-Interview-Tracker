Version 1 (Standard DSA)
Problem:
Given a list of integers nums, return a new list containing only the first occurrence of each element while preserving the original order.
You may not reorder the elements.
Function signature
def remove_duplicates(nums: list[int]) -> list[int]:
    ...

Example
Input:  [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]

Version 2 (Real-world wording — very common)
Problem
A website logs user IDs each time a user visits a page:
["u1", "u2", "u2", "u3", "u1", "u4"]
Return the list of unique users in the order of their first visit.