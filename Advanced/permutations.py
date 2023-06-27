#Permutation of a String:
import itertools

def get_permutations(string):
    perms = [''.join(perm) for perm in itertools.permutations(string)]
    return perms

# Example usage
word = "ABC"
permutations = get_permutations(word)
print(permutations)  # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
#Code BY @ Rakesh Roshan Rath