#The Number of Capital Letters in the String
def count_capital_letters(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

# Example usage
text = "Hello, World!"
capital_count = count_capital_letters(text)
print(capital_count)  # Output: 2
#Code By @Rakesh Roshan Rath