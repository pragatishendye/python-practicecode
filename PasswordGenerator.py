"""
Password Generator Program v1: Generates a password with a random number of letters, symbols and numbers.
Created by Pragathi Shendye
"""


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^']

num_letters = random.randint(1, 11)
num_symbols = random.randint(1, 6)
num_numbers = random.randint(1, 6)

pwd_list = []

for i in range(num_letters):
    pwd_list.append(random.choice(letters))

# print(pwd_list)

for i in range(num_symbols):
    pwd_list.append(random.choice(symbols))
# print(pwd_list)

for i in range(num_numbers):
    pwd_list.append(random.choice(numbers))

# print(pwd_list)

new_pwd = ''.join(pwd_list)
print(f"Your new password can be: {new_pwd}")

# More complicated password

# s = set(pwd_list)
# pwd1 = ''.join(s)

pwd1 = ''
random.shuffle(pwd_list)
for char in pwd_list:
    pwd1 += char

print(f"A more complicated form of this password can be: {pwd1}")