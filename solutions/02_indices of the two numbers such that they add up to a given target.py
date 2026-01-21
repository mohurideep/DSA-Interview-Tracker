def two_sum(nums:list[int], target:int) -> list[int]:
    lookup={}
    for i, num in enumerate(nums):
        complemet = target - num
        if complemet in lookup:
            return [i,lookup[complemet]]
        lookup[num]=i
    return []

def two_sum(nums:list[int], target:int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return None