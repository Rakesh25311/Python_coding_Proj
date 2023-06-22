#Same Subsequent Characters:
def has_same_subsequent_chars(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

# Example usage
text1 = "hello"
text2 = "world"
result1 = has_same_subsequent_chars(text1)
result2 = has_same_subsequent_chars(text2)
print(result1)  # Output: True
print(result2)  # Output: False
#Code by @Rakesh Roshan Rath