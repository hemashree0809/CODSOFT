import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for better security."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            try:
                length = int(input("Enter the desired password length: "))
                password = generate_password(length)
                print(f"Generated Password: {password}")
                print()
            except ValueError:
                print("Please enter a valid number.")
                print()
        elif choice == '2':
            print("Exiting the Password Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
            print()

if __name__ == "__main__":
    main()
