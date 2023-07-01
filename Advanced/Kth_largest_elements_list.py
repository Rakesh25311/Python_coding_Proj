#kth Largest Element in a List:
def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

# Example usage
numbers = [3, 1, 4, 2, 5]
k = 3
kth_largest = find_kth_largest(numbers, k)
print(kth_largest)  # Output: 3