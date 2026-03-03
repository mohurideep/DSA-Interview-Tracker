Problem: Longest Valid Parentheses

You are given a string s containing only the characters '(' and ')'.
Return the length of the longest contiguous substring that forms a valid parentheses sequence.

A valid parentheses sequence:
Every '(' has a matching ')'
Parentheses are properly nested

Order is correct
Function Signature
def longest_valid_parentheses(s: str) -> int:
    ...
Examples
Input:  "(()"
Output: 2
Explanation: "()"
Input:  ")()())"
Output: 4
Explanation: "()()"
Input:  ""
Output: 0
Input:  "()(()"
Output: 2