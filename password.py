import re
import random
import string
import hashlib

COMMON_PASSWORDS = [
    "password",
    "123456",
    "password123",
    "qwerty",
    "admin"
]

def calculate_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a very common password.")
        score = 0

    # Final rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    elif score <= 5:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, feedback

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage
password = input("Enter password: ")

rating, feedback = calculate_strength(password)

print(f"\nStrength: {rating}")

if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)

print("\nSuggested strong password:")
print(generate_password())

print("\nSHA-256 Hash:")
print(hash_password(password))