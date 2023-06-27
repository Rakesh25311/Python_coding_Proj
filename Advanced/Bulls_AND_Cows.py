#Bulls and Cows Problem:
def get_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    secret_count = {}
    guess_count = {}
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1
    
    for char, count in secret_count.items():
        if char in guess_count:
            cows += min(count, guess_count[char])
    
    return bulls, cows

# Example usage
secret_code = "1234"
guess_code = "12435"
bulls_count, cows_count = get_bulls_and_cows(secret_code, guess_code)
print(bulls_count)  # Output: 2
print(cows_count)  # Output: 2
#Code BY @ Rakesh Roshan Rath