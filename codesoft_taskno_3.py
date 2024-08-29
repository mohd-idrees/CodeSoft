import random
import string

def generate_pwd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(characters) for i in range(length))
    
    return pwd

def main():
    while True:
        try:

            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                pwd = generate_pwd(length)
                print(f"Generated Password: {pwd}")
            again = input("Do you want to generate another password? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
