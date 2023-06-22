#Move Zeros to End:
def move_zeros_to_end(nums):
    zeros = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * zeros)
    return nums

# Example usage
numbers = [1, 0, 2, 0, 3, 0, 4, 0]
result = move_zeros_to_end(numbers)
print(result)  # Output: [1, 2, 3, 4, 0, 0, 0, 0]
#Code by @Rakesh Roshan Rath