# Python program to check prime number
num= int(input("Enter the  number=  "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
else:
    print("Enter a positive number")