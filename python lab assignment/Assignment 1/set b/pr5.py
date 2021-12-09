# Python program to find the factorial of a number
num= int(input("Enter the number= "))
fact=1
if num<0:
    print("Please enter a positive number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact*=i
    print(f"the factorial of {num} is {fact}")