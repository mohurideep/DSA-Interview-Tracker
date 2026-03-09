#using regex
import re
def sum_numbers_in_string_regex(s):
    numbers = re.findall(r'\d+', s)
    # Convert the list of strings to integers and sum them without sum,map
    total = 0
    for n in numbers:
        total += int(n)
    return total
    # return sum(map(int, numbers))

print(sum_numbers_in_string_regex("abc123xyz456"))

#without regex
def sum_numbers_in_string_no_regex(s):
    total = 0
    current_number = ''
    
    for char in s:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total += int(current_number)
                current_number = ''
    
    # Check if there's a number at the end of the string
    if current_number:
        total += int(current_number)
    
    return total

print(sum_numbers_in_string_no_regex("abc123xyz456"))