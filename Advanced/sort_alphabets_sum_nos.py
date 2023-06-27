#Sorted Alphabets and Sum of Integers:
def sort_alphabets_and_sum_integers(string):
    alphabets = []
    integers_sum = 0
    for char in string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isdigit():
            integers_sum += int(char)
    sorted_alphabets = sorted(alphabets)
    return sorted_alphabets, integers_sum

# Example usage
text = "a1b2c3d4"
sorted_chars, sum_of_integers = sort_alphabets_and_sum_integers(text)
print(sorted_chars)  # Output: ['a', 'b', 'c', 'd']
print(sum_of_integers)  # Output: 10
#Code BY @ Rakesh Roshan Rath