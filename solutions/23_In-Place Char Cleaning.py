def remove_special_char(char : list) -> None:
    # You cannot delete elements from a list efficiently during traversal because:
    # pop / remove → shifting elements → O(n) each
    # Two-pointer compaction (or in-place filtering)
    write = 0
    for read in range(len(char)):
        if char[read].isalnum():  # Check if the character is alphanumeric
            char[write] = char[read]  # Move valid character to the write position
            write += 1  # Increment write pointer
    # return char[:write]  # Return the list up to the last valid character
    del char[write:]  # Remove all invalid characters


chars = ['a','!','b','@','c','#','1','2','3','$']

remove_special_char(chars)
print(chars)