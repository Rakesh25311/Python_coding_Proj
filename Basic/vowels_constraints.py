#The Number of Vowels and Consonants:
def count_vowels_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# Example usage
text = "Hello, World!"
vowels, consonants = count_vowels_consonants(text)
print(vowels)      # Output: 3
print(consonants)  # Output: 7
#Code by @Rakesh Roshan Rath