def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1] * n

    #step 1 build prefix product into output
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    
    #step 2 multiply suffix product into output
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output