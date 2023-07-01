#Smallest Missing Integer:
def smallest_missing_integer(nums):
    nums_set = set(nums)
    smallest = 1
    while smallest in nums_set:
        smallest += 1
    return smallest

# Example usage
numbers = [1, 3, 6, 4, 1, 2]
missing_integer = smallest_missing_integer(numbers)
print(missing_integer)  # Output: 5