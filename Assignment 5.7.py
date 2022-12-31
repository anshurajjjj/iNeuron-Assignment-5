#Write a python script which takes a three digit number from the user and displays
#only its last digit.
n=int(input("Please Enter any Number: "))
lastdigit=n % 10
print("The Last Digit in a Given Number %d = %d" %(n, lastdigit))
