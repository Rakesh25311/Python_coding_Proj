'''#Minimum Characters to Make a String a Palindrome:
#Code BY @Rakesh Roshan Rath
'''
def min_chars_to_make_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return 0
    for i in range(len(string)):
        if string[i:] == reversed_string[:len(string)-i]:
            return i

# Example usage
text = "abcd"
min_chars = min_chars_to_make_palindrome(text)
print(min_chars)  # Output: 3
