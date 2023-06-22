#Check Whether Two Strings are Anagrams:
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
anagrams = are_anagrams(string1, string2)
print(anagrams)  # Output: True
#Code by @Rakesh Roshan Rath