# Program that asks for input made of specific character types. Keeps asking until correct input is received.
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():  # Checks if input is numerical
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only)')
    password = input()
    if password.isalnum():  # Checks if input is alphanumerical.
        break
    print('Password can only have letters and numbers')