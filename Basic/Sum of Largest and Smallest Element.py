#Sum of Largest and Smallest Element
def sum_largest_smallest(nums):
    if not nums:
        return None
    smallest = min(nums)
    largest = max(nums)
    return smallest + largest

# Example usage
nums = [1, 2, 3, 4, 5]
result = sum_largest_smallest(nums)
print(result)  # Output: 6
#Code by @Rakesh Roshan Rath