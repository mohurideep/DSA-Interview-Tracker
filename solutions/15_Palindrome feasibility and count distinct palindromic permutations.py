# Problem: Palindrome Feasibility and Count Distinct Palindromic Permutations
#
# TODO:
# - Determine whether any permutation of the input string can form a palindrome.
# - If possible, compute the number of distinct palindromic permutations.
# - If not possible, the expected result is 0.
#
"""
Part 1: check whether a palindrome permutation is possible.
First, compute character frequencies.
For a palindrome permutation to exist, at most one character can have an odd frequency.
If more than one odd frequency exists, it is impossible to form a palindrome.
"""
from collections import Counter
def can_form_palindrome(s: str) -> bool:
    freq = Counter(s)
    odd_count = 0

    for count in freq.values():
        if count % 2 != 0 :
            odd_count +=1
    #atmost 1 odd allowed
    #returning boolean condition
    return odd_count <= 1



print(can_form_palindrome("abba"))


"""
Part 2: Count distinct palindromic permutations.
If a palindrome permutation is possible, we need to count the distinct palindromic permutations.
To do this, we can use the formula:
    distinct_palindromic_permutations = (n! / (c1! * c2! * ... * ck!))
Where n is the length of the string, and c1, c2, ..., ck are the frequencies of the characters.
Since a palindrome is symmetric, I only need to permute the first half.
The second half is automatically determined.
Therefore I calculate permutations of half the character counts using factorial formula for duplicates.
"""
from math import factorial
def count_palindrome_permutations(s: str) -> int:
    if not can_form_palindrome(s):
        return 0
    
    freq = Counter(s)

    #only consider half count
    half_counts = []
    for count in freq.values():
        half_counts.append(count // 2)

    half_length = sum(half_counts)

    # Calculate the numerator (half_length!)
    numerator = factorial(half_length)

    # Calculate the denominator (c1! * c2! * ... * ck!)
    denominator = 1
    for count in half_counts:
        denominator *= factorial(count)

    # Return the number of distinct palindromic permutations
    return numerator // denominator

print(count_palindrome_permutations("aabb"))  # Output: 2 (permutations: "abba", "baab")


#factorial function
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_simple(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result