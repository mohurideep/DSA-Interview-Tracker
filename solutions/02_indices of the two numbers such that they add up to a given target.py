def two_sum(nums:list[int], target:int) -> list[int]:
    lookup={}
    for i, num in enumerate(nums):
        complemet = target - num
        if complemet in lookup:
            return [i,lookup[complemet]]
        lookup[num]=i
    return []