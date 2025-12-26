import argparse
import re


def check_password_strength(password: str):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("Add at least one special character.")

    return score, tips


def strength_label(score: int) -> str:
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker")
    parser.add_argument("--password", required=True, help="Password to check")
    args = parser.parse_args()

    score, tips = check_password_strength(args.password)
    label = strength_label(score)

    print(f"Strength: {label} ({score}/5)")

    if tips:
        print("\nSuggestions:")
        for tip in tips:
            print(f"- {tip}")


if __name__ == "__main__":
    main()
