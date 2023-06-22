#Alphabets, Digits, and Symbols in a String:
def count_characters(string):
    counts = {
        'alphabets': 0,
        'digits': 0,
        'symbols': 0
    }
    for char in string:
        if char.isalpha():
            counts['alphabets'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['symbols'] += 1
    return counts

# Example usage
text = "Hello, 123!"
character_counts = count_characters(text)
print(character_counts)  # Output: {'alphabets': 5, 'digits': 3, 'symbols': 2}
#Code by @Rakesh Roshan Rath