#Before and After:
def before_and_after(string, target):
    index = string.find(target)
    if index == -1:
        return None
    before = string[:index]
    after = string[index + len(target):]
    return before, after

# Example usage
text = "Hello, World!"
target = "World"
result = before_and_after(text, target)
print(result)  # Output: ('Hello, ', '!')
#Code By @Rakesh Roshan Rath