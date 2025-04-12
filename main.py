
import re
import json
from pathlib import Path

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password):
    return len(password) >= 8

def save_registration(user_data):
    registrations_file = Path('registrations.json')
    existing_data = []
    
    if registrations_file.exists():
        with open(registrations_file, 'r') as f:
            existing_data = json.load(f)
    
    existing_data.append(user_data)
    
    with open(registrations_file, 'w') as f:
        json.dump(existing_data, f, indent=2)

def form_based_registration():
    print("--- User Registration Form ---")
    
    name = input("Enter your name: ")
    
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")
    
    while True:
        password = input("Enter your password (min 8 characters): ")
        if validate_password(password):
            break
        print("Password must be at least 8 characters long. Please try again.")
    
    age = input("Enter your age: ")
    
    user_data = {
        "name": name,
        "email": email,
        "password": password,
        "age": age
    }
    
    save_registration(user_data)
    
    print("\n--- Registration Details ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    print(f"Age: {age}")
    print("Registration successful! Details saved to registrations.json")

if __name__ == "__main__":
    form_based_registration()
