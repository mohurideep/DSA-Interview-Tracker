Problem: Flatten a Nested List

You are given a list that may contain integers or other nested lists.
Write a function that returns a flattened list containing all integers in the original order.

Function Signature
def flatten_list(nested_list: list) -> list:
    ...
Example
Input
[1, [2, 3], [4, [5, 6]], 7]

Output
[1, 2, 3, 4, 5, 6, 7]



Real Interview Version
Problem
Implement a function that takes a list that may contain nested lists of arbitrary depth and returns a single flattened list.

Example
Input:
[1, [2, [3, [4]], 5]]

Output:
[1, 2, 3, 4, 5]

Important point:depth is unknown