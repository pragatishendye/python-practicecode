"""
 This program uses a function which takes a score as it's parameter
 and returns an appropriate grade.
 Created by Pragathi Shendye
"""


def computegrade(score):
    if score < 0.0 or score > 1.0:
        print('Bad score')
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


try:
    score = float(input('Enter score:'))
except ValueError:
    print('Bad score')
else:
    computegrade(score)







