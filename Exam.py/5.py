
def merge_lists(list1, list2):
    # Combine the lists and convert to a set to remove duplicates
    merged_set = set(list1 + list2)
    
    # Convert the set back to a list
    merged_list = list(merged_set)
    
    return merged_list

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = merge_lists(list1, list2)

print(result)