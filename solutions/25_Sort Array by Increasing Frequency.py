

def frequency_sort_bruteforce(nums : list[int]) -> list[int]:
    freq_list = []
    # step 1 : compute freq for each element
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        freq_list.append((nums[i], count))

print(frequency_sort_bruteforce([2,3,1,3,2]))