#Sum of Two Elements:
def find_sum_of_two(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example usage
numbers = [2, 4, 6, 8, 10]
target_sum = 14
found_sum = find_sum_of_two(numbers, target_sum)
print(found_sum)  # Output: True