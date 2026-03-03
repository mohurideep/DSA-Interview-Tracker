#give a bruteforce soltuion of longest valid parentheses
#time complexity o(n^3)
def longest_valid_parentheses(s: str) -> int:
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1, 2):
            if is_valid(s[i:j]):
                max_length = max(max_length, j - i)
    return max_length

def is_valid(s: str) -> bool:
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


print(longest_valid_parentheses("((())"))  # Output: 4