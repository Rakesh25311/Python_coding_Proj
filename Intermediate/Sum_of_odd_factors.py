#Sum of Odd Factors:
def sum_odd_factors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            total += i
    return total

# Example usage
number = 12
odd_factors_sum = sum_odd_factors(number)
print(odd_factors_sum)  # Output: 8 (1 + 3)
#Code by @Rakesh Roshan Rath