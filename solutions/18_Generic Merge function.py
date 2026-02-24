def merge_sorted_list(arr1, arr2):
    i = 0
    j = 0
    result = []

    if type(arr1) != type(arr2):
        raise TypeError("Both inputs must be of the same type")

    #compare elements from both the array/list
    while i < len(arr1) and j < len(arr2):
        if type(arr1[i]) != type(arr2[j]):
            raise TypeError("Elements must be of the same type")
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else :
            result.append(arr2[j])
            j += 1

    # add remaining elements
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])
    return result

def read_list(input_str):
    data = input(input_str).split()
    try :
        return [int(x) for x in data]
    except ValueError:
        return data
    
arr1 = read_list("Enter elements of first sorted array separated by space: ")
arr2 = read_list("Enter elements of second sorted array separated by space: ")

merge = merge_sorted_list(arr1, arr2)
print("Merged array:", merge)