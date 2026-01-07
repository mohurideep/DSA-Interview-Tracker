Problem
Given an array prices where prices[i] is the stock price on day i, return the maximum profit you can achieve by buying once and selling once.

If no profit is possible, return 0.

Function signature
def max_profit(prices: list[int]) -> int:
    ...

Examples
[7,1,5,3,6,4] → 5   # buy at 1, sell at 6
[7,6,4,3,1]   → 0
[1,2]         → 1

Rules
Must be O(n)
Only one buy and one sell
Buy must happen before sell