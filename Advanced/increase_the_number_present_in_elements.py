#Increase Number Represented by List Elements:
def increase_number_by_value(nums, value):
    for i in range(len(nums)):
        nums[i] += value
    return nums

# Example usage
numbers = [1, 2, 3, 4, 5]
increased_numbers = increase_number_by_value(numbers, 10)
print(increased_numbers)  # Output: [11, 12, 13, 14, 15]