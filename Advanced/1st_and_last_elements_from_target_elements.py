#First and Last Index of Target Element:
def find_indices(nums, target):
    first_index = -1
    last_index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first_index == -1:
                first_index = i
            last_index = i
    return first_index, last_index

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 2]
target = 2
first, last = find_indices(numbers, target)
print(first)  # Output: 1
print(last)  # Output: 5