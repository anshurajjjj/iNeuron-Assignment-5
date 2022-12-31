#Write a python script which takes a three digit number from the user and displays only its middle digit.
# take input
num = int(input('Enter any Number: '))

# get the middle digit
while (num >= 100):
    num = num //100

# printing middle digit of number
print('The middle digit of number:', num)
