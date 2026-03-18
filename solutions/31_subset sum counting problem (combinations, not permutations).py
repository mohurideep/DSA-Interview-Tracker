#backtracking method
def countCombinations(nums: list[int], target: int) -> int:
    def backtrack(start: int, current_sum: int) -> int:
        if current_sum == target:
            return 1
        if current_sum > target or start == len(nums):
            return 0
        # Include the current number
        include = backtrack(start + 1, current_sum + nums[start])
        # Exclude the current number
        exclude = backtrack(start + 1, current_sum)
        return include + exclude

    return backtrack(0, 0)

print(countCombinations([1, 2, 3, 4, 5], 5))  # Output: 3

#simple Bruteforce method
def countCombinationsBruteForce(nums, target):
    n = len(nums)
    count = 0

    for mask in range(1 << n):  # 2^n subsets
        current_sum = 0

        for i in range(n):
            if mask & (1 << i):   # include nums[i]
                current_sum += nums[i]

        if current_sum == target:
            count += 1

    return count

print(countCombinationsBruteForce([1, 2, 3, 4, 5], 5))  # Output: 3