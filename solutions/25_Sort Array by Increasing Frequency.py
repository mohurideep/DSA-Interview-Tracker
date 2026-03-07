

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
    result = [num for num, _ in freq_list]

    # #Equivallent line
    # for num, _ in freq_list:
    #     result.append(num)

    return result

print(frequency_sort_bruteforce([2,3,1,3,2]))



def frequency_sort_hashmap(nums : list[int]) -> list[int]:
    freq_map = {}
    for n in nums:
        freq_map[n] = freq_map.get(n, 0) + 1

    # sort by freq ascending, value descending
    sorted_freq = sorted(freq_map.items(), key = lambda x: (x[1], -x[0]))

    result = [num for num, _ in sorted_freq]

    return result

print(frequency_sort_hashmap([2,3,1,3,2]))