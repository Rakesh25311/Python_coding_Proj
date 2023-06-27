#Thousand Separator:
def thousand_separator(number):
    number_str = str(number)
    separator = ','
    if len(number_str) <= 3:
        return number_str
    result = ''
    for i in range(len(number_str)):
        if i > 0 and (len(number_str) - i) % 3 == 0:
            result += separator
        result += number_str[i]
    return result

# Example usage
num = 1234567890
formatted_num = thousand_separator(num)
print(formatted_num)  # Output: "1,234,567,890"
#Code BY @ Rakesh Roshan Rath