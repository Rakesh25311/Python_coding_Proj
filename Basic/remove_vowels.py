#Remove Vowels From a String:
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for char in string:
        if char.lower() not in vowels:
            result += char
    return result

# Example usage
text = "Hello, World!"
result = remove_vowels(text)
print(result)  # Output: "Hll, Wrld!"
#Code by @Rakesh Roshan Rath