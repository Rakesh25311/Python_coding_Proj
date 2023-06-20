#Sorted Words in a String:
def sorted_words(string):
    words = string.split()
    sorted_words = sorted(words)
    return sorted_words

# Example usage
sentence = "Hello, how are you today?"
sorted_word_list = sorted_words(sentence)
print(sorted_word_list)  # Output: ['Hello,', 'are', 'how', 'today?', 'you']
#Code By @Rakesh Roshan Rath