#Remove Duplicate Characters in the String:
def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

# Example usage
text = "Hello, World!"
result = remove_duplicates(text)
print(result)  # Output: "Helo, Wrd!"
#Code by @Rakesh Roshan Rath