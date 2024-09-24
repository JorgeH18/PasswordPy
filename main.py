import random, string, math, re, secrets, hashlib
from cryptography.fernet import Fernet

# Password encrypt
def encrypt_password(password, key):

    # Instance the Fernet class with the key
    fernet = Fernet(key)
    # to encrypt the string must be encoded to byte string
    encryptedPassword = fernet.encrypt(password.encode())
    return encryptedPassword


# Password decrypt
def decrypt_password(encryptedPassword, key):

    # Instance the Fernet class with the key
    fernet = Fernet(key)
    # decrypt with the instance of the key that was used for encrypting the string and decode back to string
    decryptedPassword = fernet.decrypt(encryptedPassword).decode()
    return decryptedPassword


# Generates a strong password with the specified criteria
def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    characters = []
    specCharacters = "£$&()*+[]@#^!?";
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_lowercase:
        characters.extend(string.ascii_lowercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special_chars:
        characters.extend(specCharacters)

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
    if re.search(r"[£$&()*+[\]@#^!?]", password):
        possible_characters += 14

    length = len(password)
    # Do calculation
    entropy = math.log2(possible_characters) * length
    return round(entropy,2)



# Defining main function
def main():

    # Generate a key for encryption and decryption
    key = Fernet.generate_key()

    # Password dictionary
    passwords = {}

    # Main menu
    while True:
        print("Options:")
        print("0. Generate password")
        print("1. Add password")
        print("2. Retrieve password")
        print("3. List passwords")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '0':
            website = input("Enter the website: ")
            passLen = int(input("Enter the password desired lenght: "))
            password = generate_password(passLen)
            entropy = calculate_entropy(password)
            encryptedPassword = encrypt_password(password,key)
            passwords[website] = encryptedPassword
            print("Password added successfully.")
            print("Entropy:", entropy)

        elif choice == '1':
            website = input("Enter the website: ")
            password = input("Enter the password: ")
            entropy = calculate_entropy(password)
            encryptedPassword = encrypt_password(password,key)
            passwords[website] = encryptedPassword
            print("Password added successfully.")
            print("Entropy:", entropy)

        elif choice == '2':
            website = input("Enter the website: ")
            if website in passwords:
                encryptedPassword = passwords[website]
                decryptedPassword = decrypt_password(encryptedPassword,key)
                print("Decrypted password:", decryptedPassword)
            else:
                print("Website not found.")

        elif choice == '3':
            print("Stored passwords:")
            for website in passwords:
                print(website, passwords[website])

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__=="__main__":
    main()