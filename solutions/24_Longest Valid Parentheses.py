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


# print(longest_valid_parentheses("((())"))  # Output: 4

#time complexity o(n^2)

def longest_valid_parentheses_dp(s: str) -> int:
    max_length = 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0) + 2
            max_length = max(max_length, dp[i])
    return max_length


#time complexity o(n)
def longest_valid_parentheses_stack(s: str) -> int:
    max_length = 0
    stack = [-1]
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

print(longest_valid_parentheses_stack(")()())"))  # Output: 4