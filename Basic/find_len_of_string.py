#Find the Length of the String Without the len() Function:
def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count

# Example usage
text = "Hello, World!"
length = string_length(text)
print(length)  # Output: 13
#Code by @Rakesh Roshan Rath