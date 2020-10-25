"""
This program prompts the user for a temperature in Fahrenheit and returns
the Celsius equivalent of it.
Created by Pragathi Shendye
"""

tempInFahrenheit = float(input('Enter a temperature in Fahrenheit:'))
tempInCelsius = (tempInFahrenheit - 32) * (5 / 9)
print('{} Fahrenheit = {:.2f} Celsius'.format(tempInFahrenheit, tempInCelsius))