#Uppercase Letters in a String:
def uppercase_letters(string):
    uppercase = [char for char in string if char.isupper()]
    return uppercase

# Example usage
text = "Hello, World!"
uppercase_letters = uppercase_letters(text)
print(uppercase_letters)  # Output: ['H', 'W']
#Code By @Rakesh Roshan Rath