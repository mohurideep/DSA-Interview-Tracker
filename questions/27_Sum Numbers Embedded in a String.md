You are given a string s containing a mix of letters and digits.
Numbers may appear anywhere in the string as continuous sequences of digits.

Your task is to:
Extract all the numbers from the string.
Convert them into integers.
Return the sum of those numbers.

Function Signature
def sum_numbers_in_string(s: str) -> int:
Example

Input:
s = "B200E111B10"

Extracted numbers:
200, 111, 10

Output:
321