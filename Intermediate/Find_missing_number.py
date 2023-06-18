#Find a Missing Number From a List
def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number

# Example usage
numbers = [1, 2, 4, 5, 6]
missing_num = find_missing_number(numbers)
print(missing_num)  # Output: 3
#Code by @Rakesh Roshan Rath