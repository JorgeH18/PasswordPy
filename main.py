import random, string, math, re

# Generates a strong password with the specified criteria
def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    characters = []
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_lowercase:
        characters.extend(string.ascii_lowercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special_chars:
        characters.extend(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Calculate entropy taking possible characters and password length
def calculate_entropy(password):
    # First count the possible characters
    possible_characters = 0
    if re.search(r"[A-Z]", password):
        possible_characters += 26
    if re.search(r"[a-z]", password):
        possible_characters += 26
    if re.search(r"\d", password):
        possible_characters += 10
    if re.search(r"[^A-Za-z0-9]", password):
        possible_characters += 32

    length = len(password)
    # Do calculation
    entropy = math.log2(possible_characters) * length
    return round(entropy,2)



# Defining main function
def main():
    password = generate_password()
    entropy = calculate_entropy(password)
    print("Password:", password)
    print("Entropy:", entropy)


if __name__=="__main__":
    main()