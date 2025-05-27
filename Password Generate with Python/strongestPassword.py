import random
# A function that generate a stronger password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'
]

print('Welcome to the new strong password generate program!')
print('Please answer this questions below to give a strong password!')

user_letters = int(input('How much letter do you like in your password? \n'))
user_numbers = int(input('How much numbers do you like in your password? \n'))
user_symbols = int(input('How much symbols do you like in your password? \n'))

# Easy Mode
# password = ''
# for char in range(0, user_letters):
#     password += random.choice(letters)
# for char in range(0, user_numbers):
#     password += random.choice(numbers)
# for char in range(0, user_symbols):
#     password += random.choice(symbols)
#
# print(f'Your random password is: {password}')

# Hard Mode
password_list = []
for char in range(0, user_letters):
    password_list += random.choice(letters)
for char in range(0, user_numbers):
    password_list += random.choice(numbers)
for char in range(0, user_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ''

for char in password_list:
    password += char

print(f'Your random password is: {password}')
