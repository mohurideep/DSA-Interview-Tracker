

def frequency_sort_bruteforce(nums : list[int]) -> list[int]:
    freq_list = []
    # step 1 : compute freq for each element
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        freq_list.append((nums[i], count))

     # Step 2: sort by frequency asc, value desc
    freq_list.sort(key=lambda x: (x[1], -x[0]))

    # Step 3: rebuild the array
    result = [num for num, freq in freq_list]

    return result

print(frequency_sort_bruteforce([2,3,1,3,2]))