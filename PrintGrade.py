"""
This program takes a score between 0.0 and 1.0 and prints a grade accordingly.
Created by Pragathi Shendye
"""

errorMsg = 'Bad score'

try:
    score = float(input('Enter score:'))
except ValueError:
    print(errorMsg)
else:
    if score < 0.0 or score > 1.0:
        print(errorMsg)
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')



