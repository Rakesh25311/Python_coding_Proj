#Secret Message:
def extract_secret_message(string):
    secret_message = ''
    for char in string:
        if char.isupper():
            secret_message += char
    return secret_message

# Example usage
text = "H3lloW0rld"
message = extract_secret_message(text)
print(message)  # Output: "HW"