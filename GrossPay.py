"""
This program prompts the user for hours and rate per hour and computes
the gross pay.
If the number of hours worked is above 40, the pay is 1.5 times the per hour rate for those hours.
Created by Pragathi Shendye
"""

try:
    hoursWorked = int(input('Enter number of hours worked: '))
    ratePerHour = float(input('Enter the rate per hour: '))
except ValueError:
    print('Error! Please enter numeric input')
else:
    normalHours = 40
    overtimeFactor = 1.5

    if hoursWorked > normalHours:
        grossPay = ((hoursWorked - normalHours) * overtimeFactor * ratePerHour) + (normalHours * ratePerHour)
    else:
        grossPay = hoursWorked * ratePerHour

    print('Pay: {}'.format(grossPay))

