"""
This program keeps prompting the user to enter numbers until they are done and then
returns the maximum and minimum values entered by the user.
Created by Pragathi Shendye
"""

l_nums = list()

while True:
    userInput = input('Enter a number:')
    if userInput == 'done':
        break
    else:
        try:
            l_nums.append(int(userInput))
        except ValueError:
            print('Invalid input')

# Calculate the minimum and maximum of numbers entered
minimum, maximum = None, None

for num in l_nums:
    if minimum is None or num < minimum:
        minimum = num

for num in l_nums:
    if maximum is None or num > maximum:
        maximum = num

print('Maximum:{}, Minimum:{}'.format(maximum, minimum))
