import random

# Define the characters to use for the password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='

# Ask the user for the length of the password they want to generate
length = int(input("Enter the desired password length: "))

# Initialize an empty string for the password
password = ""

# Loop through the desired length of the password and add a random character from the chars string each time
for i in range(length):
    password += random.choice(chars)

# Print the generated password
print("Your randomly generated password is:", password)
