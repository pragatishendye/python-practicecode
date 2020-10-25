"""
This program prompts the user for a temperature in Celsius and returns
the Fahrenheit equivalent of it.
Created by Pragathi Shendye
"""

tempInCelsius = float(input('Enter a temperature in Celsius:'))
tempInFahrenheit = tempInCelsius * (9 / 5) + 32
print(f'The temperature in Fahrenheit is: {tempInFahrenheit}')