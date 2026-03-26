import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase length to at least 8 characters.")

    # Rule 2: Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Rule 3: Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 4: Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Rule 5: Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%).")

    # Output the results
    print("\n--- 🔐 Password Analysis ---")
    if score == 5:
        print("Strength: Strong 💪")
        print("Great job! This is a secure password.")
    elif score >= 3:
        print("Strength: Moderate ⚠️")
        print("Suggestions to improve:")
        for item in feedback:
            print(f" - {item}")
    else:
        print("Strength: Weak ❌")
        print("Suggestions to improve:")
        for item in feedback:
            print(f" - {item}")

def main():
    print("Welcome to the Password Complexity Checker")
    user_password = input("Enter a password to test: ")
    check_password_strength(user_password)

if __name__ == "__main__":
    main()