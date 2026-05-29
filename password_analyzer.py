# Password Strength Analyzer

password = input("Enter your password: ")

strength = 0

# Check password length
if len(password) >= 8:
    strength += 1

# Check uppercase letter
if any(char.isupper() for char in password):
    strength += 1

# Check lowercase letter
if any(char.islower() for char in password):
    strength += 1

# Check number
if any(char.isdigit() for char in password):
    strength += 1

# Check special character
special_chars = "!@#$%^&*()_+-="
if any(char in special_chars for char in password):
    strength += 1

# Result
if strength <= 2:
    print("Weak Password")
elif strength == 3 or strength == 4:
    print("Medium Password")
else:
    print("Strong Password")
