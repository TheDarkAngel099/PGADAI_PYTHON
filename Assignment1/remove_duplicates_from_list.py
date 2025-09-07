def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original_list = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", original_list)
print("List after removing duplicates:", remove_duplicates(original_list))
