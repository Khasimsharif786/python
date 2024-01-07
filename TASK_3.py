import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    """Generate a random password based on user-defined criteria."""
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        include_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, include_letters, include_numbers, include_symbols)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Invalid input for password length.")
