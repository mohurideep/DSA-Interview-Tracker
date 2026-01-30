def subarray_sum_count(nums:list[int], k:int) -> int:
    prefix_sum=0
    count=0
    prefix_map ={0:1}

    for num in nums:
        prefix_sum += num

        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum-k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0)+1

    return count


def subarray_sum_count1(nums: list[int], k:int) -> int:
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers.")
    count =0
    n = len(nums)
    for i in range(n):
        for j in range(i,n):
            if sum(nums[i:j+1]) == k:
                count += 1
    return count

print(subarray_sum_count([0,0,0],0))  # Output: 2