#Check Whether the String is a Palindrome or Not
def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

# Example usage
word = "radar"
result = is_palindrome(word)
print(result)  # Output: True
#Code by @Rakesh Roshan Rath