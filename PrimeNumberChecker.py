"""
This program checks whether a given number is prime or not.
Created by Pragathi Shendye
"""


def prime_checker(number):
  half_mark = number // 2
  prime = True
  for i in range(2, half_mark+1):
    if number % i == 0:
      prime = False

  if prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


num = int(input("Enter a number: "))
prime_checker(num)