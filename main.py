
def form_based_registration():
    print("--- User Registration Form ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    age = input("Enter your age: ")
    
    print("\n--- Registration Details ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    print(f"Age: {age}")
    print("Registration successful!")

if __name__ == "__main__":
    form_based_registration()
