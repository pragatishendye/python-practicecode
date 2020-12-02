"""
Password Generator Program v2: Generates a random password with a given number of letters, symbols and numbers
as selected by the user.
Created by Pragathi Shendye
"""


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^']

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

pwd_list = []

for i in range(num_letters):
    pwd_list.append(random.choice(letters))

for i in range(num_symbols):
    pwd_list.append(random.choice(symbols))

for i in range(num_numbers):
    pwd_list.append(random.choice(numbers))

new_pwd = ''.join(pwd_list)
print(f"Your new password can be: {new_pwd}")

# More complicated password

pwd1 = ''
random.shuffle(pwd_list)
for char in pwd_list:
    pwd1 += char

print(f"A more complicated form of this password can be: {pwd1}")