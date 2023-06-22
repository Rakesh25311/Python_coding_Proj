#Length of the Last Word in a String:Copy code
def length_of_last_word(string):
    words = string.split()
    if len(words) > 0:
        return len(words[-1])
    else:
        return 0

# Example usage
text = "Hello, World!"
last_word_length = length_of_last_word(text)
print(last_word_length)  # Output: 6
#Code by @Rakesh Roshan Rath