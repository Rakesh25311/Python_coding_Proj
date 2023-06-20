#Middle Letter:
def middle_letter(string):
    length = len(string)
    if length % 2 == 0:
        return string[length // 2 - 1: length // 2 + 1]
    else:
        return string[length // 2]

# Example usage
word1 = "Hello"
word2 = "Python"
middle1 = middle_letter(word1)
middle2 = middle_letter(word2)
print(middle1)  # Output: "l"
print(middle2)  # Output: "t"
#Code By @Rakesh Roshan Rath