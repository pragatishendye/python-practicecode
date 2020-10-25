"""
 This program prompts the user to enter numbers until the string 'done' is typed.
 Returns the count of numbers entered, their total and average.
 Created by Pragathi Shendye
"""

count, total, average = 0, 0, 0

while True:
    userInput = input('Enter a number: ')
    if userInput == 'done':
        break
    else:
        try:
            num = int(userInput)
        except ValueError:
            print('Invalid input')
        else:
            count += 1
            total += num

try:                                    # Handles the case where user enters 'done' on the first instance itself
    average = total / count
except ZeroDivisionError:
    print('No numbers entered')
print(f'Total:{total} Count:{count} Average:{average}')

