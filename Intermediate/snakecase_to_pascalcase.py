#Convert snake_case to PascalCase:
def convert_snake_to_pascal(snake_case):
    words = snake_case.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

# Example usage
snake_case_str = "hello_world_example"
pascal_case_str = convert_snake_to_pascal(snake_case_str)
print(pascal_case_str)  # Output: "HelloWorldExample"
#Code by @Rakesh Roshan Rath