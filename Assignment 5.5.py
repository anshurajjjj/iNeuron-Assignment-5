#Write a python script which takes a three digit number from the user and displays
#only its middle digit.
from math import log10
n=int(input("Enter any three digit number"))
digit_count = int(log10(n)) + 1
middle = digit_count // 2
print(n // 10 ** middle % 10)
