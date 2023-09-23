import random
import string
import pyperclip

def generate_password(length=12, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets based on user's choice
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Check if the length is valid
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    generated_password = generate_password(password_length, include_special)
    if generated_password:
        # Copy the generated password to the clipboard
        pyperclip.copy(generated_password)
        print("Generated Password:", generated_password)
        print("Password copied to clipboard.")
