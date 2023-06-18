#Find Duplicate Elements in the List
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 7, 5]
duplicate_nums = find_duplicates(numbers)
print(duplicate_nums)  # Output: [2, 3, 5]
#Code by @Rakesh Roshan Rath