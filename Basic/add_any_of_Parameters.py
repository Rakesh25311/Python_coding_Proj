#Add Any Number of Parameters:
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example usage
result = add_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15
#Code By @Rakesh Roshan Rath