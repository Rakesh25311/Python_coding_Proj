#Increase Values in a Dictionary:
def increase_dictionary_values(dictionary, increase_by):
    for key in dictionary:
        dictionary[key] += increase_by

# Example usage
my_dict = {"a": 1, "b": 2, "c": 3}
increase_by = 2
increase_dictionary_values(my_dict, increase_by)
print(my_dict)  # Output: {"a": 3, "b": 4, "c": 5}
#Code By @Rakesh Roshan Rath