import re

def check_strength(password):
    score = 0
    suggestion = []

    if len(password) >= 8:
        score += 1
    else:
        suggestion.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    # uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestion.append("Add uppercase letters")

    # lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestion.append("Add lowercase letters")

    # digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestion.append("Add digits")

    # special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestion.append("Add special characters")

    # strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestion


def main():
    print("PASSWORD STRENGTH CHECKER")

    password = input("ENTER YOUR PASSWORD: ")
    strength, tips = check_strength(password)

    print(f"\nStrength: {strength}")

    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print("-", tip)


if __name__ == "__main__":
    main()
