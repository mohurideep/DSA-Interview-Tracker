Version 1 (Most Standard)

You are given two sorted integer arrays arr1 and arr2.
Return a new array that contains all elements from both arrays in sorted order.

Constraints

Arrays are already sorted in ascending order

Do not use built-in sorting functions

Try to achieve optimal time complexity

Function signature

def merge_sorted_lists(arr1: list[int], arr2: list[int]) -> list[int]:
    ...

Example

Input:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]


Version 2 (More Interview-ish / FAANG style)

Problem

Two sorted arrays are stored on disk and are too large to sort again.
Design an algorithm to combine them into a single sorted sequence efficiently.

(This wording pushes you to O(n + m) instead of sorting again.)