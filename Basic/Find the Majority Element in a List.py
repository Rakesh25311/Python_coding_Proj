#FInd the majority elements in a list
def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num
    return None

# Example usage
nums = [1, 2, 2, 2, 3, 4, 2]
majority = majority_element(nums)
print(majority)  # Output: 2
#Code by @Rakesh Roshan Rath