# Password Strength Analyzer

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Uppercase check
if any(char.isupper() for char in password):
    strength += 1

# Lowercase check
if any(char.islower() for char in password):
    strength += 1

# Number check
if any(char.isdigit() for char in password):
    strength += 1

# Special character check
special = "!@#$%^&*"

if any(char in special for char in password):
    strength += 1

# Final result
if strength <= 2:
    print("Weak Password")

elif strength <= 4:
    print("Medium Password")

else:
    print("Strong Password")
