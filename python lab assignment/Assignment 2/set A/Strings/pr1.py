# Python program to check if a string is pallindrome or not
str1= input("Enter the string= ")
if str1 == str1[::-1]:
    print("The given string is pallindrome")
else:
    print("The given string is not pallindrome")