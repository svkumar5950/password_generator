''' This is an application for generating random passwords using Python.
    This application can generate numerous passwords at once with
    custom number of password digits and also with the possibility to
    have passwords with or without any special characters.'''

import random

# Greetings
print('Hello, Welcome to the Password generator!')

# Storing the number of passwords into a variable
n_passwords = input('Please enter the number of Passwords you need:')

# This while loops are used to validate all the answers
# To validate - number of passwords
is_n_valid = True
while is_n_valid:
    try:
        if (int(n_passwords) >= 1):
            digits_password = input(
                'Please enter the number of character\'s for each password (min - 4 characters):')
            is_n_valid = False
        elif (int(n_passwords) < 1):
            n_passwords = input('Please provide a number, that is greater than 0!:')
        elif (isinstance(n_passwords, str)):
            n_passwords = input('Please provide a number!:')
    except:
        n_passwords = input('Please enter the number of Passwords you need:')

# To validate - number of digits in each passwords
is_d_valid = True
while is_d_valid:
    try:
        if (int(digits_password) >= 4):
            s_char = input(
                'Please select, if you want special character\'s in '
                'your password [Y/N]:')
            is_d_valid = False
        elif (int(digits_password) < 4):
            digits_password = input(
                'Please provide a number, that is at least 4!:')
        elif (isinstance(digits_password, str)):
            digits_password = input(
                'Please provide a number!:')
    except:
        digits_password = input(
            'Please enter the number of character\'s for each password (min - 4 characters):')

# To validate - if special characters are requiered
is_schar_valid = True
want_schar = True
while is_schar_valid:
    try:
        if (str(s_char) == 'Y') or (str(s_char) == 'y'):
            is_schar_valid = False
        elif (str(s_char) == 'N') or (str(s_char) == 'n'):
            want_schar = False
            is_schar_valid = False
        else:
            s_char = input(
                'Please select [Y/N] or [y/n]:')
    except:
        s_char = input(
            'Please select, if you want special character\'s in '
            'your password [Y/N]:')


# Initializing the characters for the password
cap_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters = 'abcdefghijklmnopqrstuvwxyz'
num_char = '0123456789'
special_char = '!@#$%^&*_'

# List of character types - to select or unselect special charcters
chars = [cap_letters, small_letters, num_char, special_char]

# Custom function to generate password
def password_gen(times, n_schar, want_char):
    passwords = []
    for x in range(int(times)):
        password = ''
        for y in range(int(n_schar)):
            char_type = 0
            if want_char:
                char_type = chars[random.randrange(len(chars))]
            else:
                char_type = chars[random.randrange(len(chars) - 1)]

            password += char_type[random.randrange(len(char_type))]

        passwords.append(password)

    for i in passwords:
        print(i)

# Pre-defined texts for the output passwords
print('Here are you passwords:\n')
if want_schar:
    print('A total of {} passwords, each consists of {} characters with special '
          'characters.\n'.format(n_passwords, digits_password))
else:
    print('A total of {} passwords, each consists of {} characters without any special '
          'characters.\n'.format(n_passwords, digits_password))

# Generating the passwords
password_gen(n_passwords,digits_password, want_schar)