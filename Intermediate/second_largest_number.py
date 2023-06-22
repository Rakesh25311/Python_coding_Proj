#Find the Second-Largest Number in a List
def find_second_largest(nums):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Example usage
numbers = [1, 5, 2, 9, 10, 7]
second_largest_num = find_second_largest(numbers)
print(second_largest_num)  # Output: 9
#Code by @Rakesh Roshan Rath