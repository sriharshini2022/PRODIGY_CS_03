import re

def passwordstrength(password):
    num = any(char.isdigit() for char in password)
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    lenreq = len(password) >= 8
    spch = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    satisfied = sum([num, upper, lower, lenreq, spch])
    if satisfied == 5:
        return "Password Strength: Very Strong ."
    elif satisfied == 4:
        return "Password Strength: Strong."
    elif satisfied == 3:
        return "Password Strength : Moderate ."
    else:
        return "Password Strength : Weak ."

def main():
    rules = [
        "1. Length: at least 12 characters.",
        "2. Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words.",
        "4. Avoid using names, birthdays, or personal details.",
        "5. Use Passwordphrases.",
        "6. Don't reuse passwords across multiple accounts.",
        "7. Change passwords regularly.",
        "8. Use Two-Factor Authentication .",
        "9. Avoid entering passwords on suspicious sites.",
        "10. use Password Manager"
    ]
    for rule in rules:
        print(rule)
    inp = input("\nEnter your password: ")
    if len(inp) > 2:
        mpassword = inp[0] + '#' * (len(inp) - 2) + inp[-1]
    else:
        mpassword = inp
    res = passwordstrength(inp)
    print("\nEntered Password: {}".format(mpassword))
    print("")
    print(res)

if __name__ == "__main__":
    main()


