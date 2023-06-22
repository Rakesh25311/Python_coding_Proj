#Reverse a String Word by Word:
def reverse_words(string):
    words = string.split()
    reversed_string = " ".join(reversed(words))
    return reversed_string

# Example usage
sentence = "Hello, how are you?"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)  # Output: "you? are how Hello,"
#Code by @Rakesh Roshan Rath