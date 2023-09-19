import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+=-{}[]|\:;"<>,.?/'

    # Combine character sets based on complexity preference
    complexity_choice = input("Choose password complexity (easy/medium/hard): ")
    if complexity_choice == 'easy':
        characters = lowercase_letters + digits
    elif complexity_choice == 'medium':
        characters = lowercase_letters + uppercase_letters + digits
    elif complexity_choice == 'hard':
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        print("Invalid complexity choice. Using medium complexity.")
        characters = lowercase_letters + uppercase_letters + digits

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length should be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
